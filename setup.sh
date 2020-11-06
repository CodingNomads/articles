mkdir -p ~/Documents/codingnomads/article-dev
cd ~/Documents/codingnomads/article-dev
git clone https://github.com/CodingNomads/article-drafts.git
cd article-drafts
git remote add production https://github.com/CodingNomads/articles.git
git pull origin main
git pull production main
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Confirm you're in: 'source venv/bin/activate'"
echo "Then run: 'python3 prepare.py <filename> -toc'"
echo "This will clean all links and add a TOC to the file"