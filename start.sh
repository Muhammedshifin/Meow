if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Muhammedshifin/Meow.git /Meow
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Meow
fi
cd /Meow
pip3 install -U -r requirements.txt
echo "Starting ᗩᒍᗩ᙭....🔥"
python3 bot.py
