# Documentation

## Updating Pages

1. Navigate to the post directory
2. `pandoc -i post.md -o post.html`

## Running Locally

1. `source .venv/bin/activate`
2. `python3 main.py`

## Configuring `nginx`

First, create an `nginx` configuration in `/etc/nginx/sites-available/`:

```
server {
    listen 80;
    server_name <URL> www.<URL>;

    location / {
        proxy_pass http://127.0.0.1:5000;  # For Gunicorn
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

```

Then, symlink the configuration file to `/etc/nginx/sites-enabled/`:

```
sudo ln -s /etc/nginx/sites-available/yourapp.conf /etc/nginx/sites-enabled/
```

Verify the configuration using `sudo nginx -t`.

Next, add an A record on Cloudflare that points to the IP address of the VM.

Use certbot to generate and install an SSL certificate:

```
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Then, create a new `systemd` service for your application in `/etc/systemd/system`:

```
[Unit]
Description=Gunicorn instance to serve <APP>
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/<APP>
Environment="PATH=/var/www/<APP>/venv/bin"
ExecStart=/var/www/<APP>/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 wsgi:app

[Install]
WantedBy=multi-user.target
```

Make sure that your application has a `wsgi.py` file for starting Gunicorn.

Debugging advice:

- View `nginx` logs: `sudo tail -n 50 /var/log/nginx/error.log`
- View service logs: `sudo journalctl -u <APP> -n 50 --no-pager`

## Automated Deployment

### Create a 'deploy' User

On the VM:

1. Create a 'deploy' user: `useradd -m -s /bin/bash deploy`
2. Set the password to 'deploy': `passwd -l deploy`
3. Create the `ssh` folder: `mkdir -p ~deploy/.ssh && chmod 700 ~deploy/.ssh`

On the workstation:

1. View all public keys: `ls ~/.ssh/*.pub`
2. Copy your public key: `cat ~/.ssh/<KEY_FILE>.pub`

On the VM:

1. Authorize the key: `echo '<KEY_CONTENT>' > ~deploy/.ssh/authorized_keys`
2. Set file permissions: `chmod 600 ~deploy/.ssh/authorized_keys`
3. Set file ownership: `chown -R deploy:deploy ~deploy/.ssh`

### Create a Bare Repository for Receiving Pushes

1. Create the directory: `sudo mkdir -p /srv/www/site.git`
2. Set ownership: `sudo chown -R deploy:deploy /srv/www/site.git`
3. Initialize a `git` repository: `sudo -u deploy git init --bare /srv/www/site.git`

### Create Working Tree for Serving Files

1. Create the directory: `sudo mkdir -p /var/www/personal-website`
2. Set ownership: `sudo chown -R deploy:deploy /var/www/personal-website`

### Create Post-Receive Hook

Create a file `/srv/www/site.git/hooks/post-receive` with the following content:

```
#!/usr/bin/env bash
set -euo pipefail

# Branch to deploy
TARGET_BRANCH="master"

# Working tree (web root or source dir)
WORK_TREE="/var/www/personal-website"
REPO_DIR="/srv/www/site.git"

read oldrev newrev refname
branch="${refname#refs/heads/}"

if [[ "$branch" != "$TARGET_BRANCH" ]]; then
  echo "Skipping deploy for branch '$branch' (only '$TARGET_BRANCH' is deployed)."
  exit 0
fi

echo "[deploy] Checking out $branch to $WORK_TREE"
GIT_WORK_TREE="$WORK_TREE" GIT_DIR="$REPO_DIR" git checkout -f "$branch"

# Reload Nginx to pick up new static files or config:
echo "[deploy] Reloading nginx"
sudo /usr/bin/systemctl reload nginx

# Restart application service:
echo "[deploy] Restarting application service"
sudo /usr/bin/systemctl restart myapp.service

echo "[deploy] Done"
```

Make the file executable: `sudo chmod +x /srv/www/site.git/hooks/post-receive`.

Give the 'deploy' user administrator privileges:

1. Edit `/etc/sudoers` as the root user.
2. Add `deploy ALL=(ALL) NOPASSWD: ALL` to the bottom of the file.

### Configure the Workstation Repository

On the workstation, add the bare repository as a remote. Then push to master.

```
git remote add prod deploy@<vm-host-or-ip>:/srv/www/site.git
git push prod master
```



