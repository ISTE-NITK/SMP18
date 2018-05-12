## Instructions to submit assignments

**1) Fork the repository.**

**2) Clone the forked repo:**

    git clone https://github.com/your-username/SMP18.git

**3) Change directory and create a folder with your name.**
Inside the folder create a text file with your details.

    cd SMP18
    cd Week-<X> // where X corresponds to the week number
    mkdir your-name
    cd your-name

**4) Add and commit changes. Push it to your repository.**

    git add .	// adds all files
    git commit -m "Your message"
    git push origin master

**5) Login to github and send a pull request to *ISTE-NITK/SMP18****
To configure upstream:

    git remote add upstream https://github.com/ISTE-NITK/SMP18.git
    
To pull the latest changes:

    git fetch upstream
    git checkout master
    git merge upstream/master

