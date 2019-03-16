#data
sudo apt update
sudo apt install python3-pip unzip
pip3 install numpy gunicorn Flask
git clone https://github.com/USF-MSDS692/recommender-jyotipmahes.git
cd recommender-parrt
wget https://s3-us-west-1.amazonaws.com/msan692/glove.6B.300d.txt.zip
wget https://s3-us-west-1.amazonaws.com/msan692/bbc.zip
unzip glove.6B.300d.txt.zip
unzip bbc.zip
gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

