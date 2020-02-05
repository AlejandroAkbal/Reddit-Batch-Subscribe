# Reddit Batch Subscribe, in python
Process a batch of subreddits, subscribing to each of them

## Requirements
- Python3
- Pip3
- Dependencies in requirements.txt

## Setup
First, create authentification [following this instructions](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps).

Then, execute the following commands

```bash
git clone https://github.com/VoidlessSeven7/Reddit-Batch-Subscribe.git

cd Reddit-Batch-Subscribe

cp .env.example .env

pip3 install -r requirements.txt
```

Edit `.env` to include credentials
Edit `list.txt` to include the subreddits you want to subscribe to

And run it

`python3 ./main.py`
