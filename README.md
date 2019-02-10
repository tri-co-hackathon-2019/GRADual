# For the 2019 TriCo Hackathon: Gradual

This is a project created for the Spring 2019 TriCo Hackathon. We wanted to create a site that, in just a few clicks, students can use to map out their entire four years!

## Authors
* **Jason Ngo** - *Back-end work*
* **Blien Habtu** - *Back-end work*
* **Iryna Khovryak** - *Front-end work* 	
* **Bella Muno** - *Front-end work*
* **Ziyao (Claire) Wang** - *Front-end work*

## Getting Started
### Prerequisites
- `Python 3.6`
- `pip`
- `virtualenv`

### Installing
First, clone the repository to your local machine
```
$ git clone https://github.com/ngojason9/GRADual
```
Next, go to the directory and create a new Python 3 virtual enviroment `$ virtualenv -p python3 env`.

Then, activate the virtual environment. If you are on Linux/MacOS, use the command `$ source env/bin/activate`. If you are on Windows, use `$ env\Scripts\activate`.

Finally, install all dependencies via the command
```
$ pip install -r requirements.txt
```

### Usage
Now that you have installed all the dependencies, run the command `$ flask run` in the virtual environment to test the application.


## Running the site

The site prompts the student to input a major. Then it auto-populates a table with the introductory classes of the major. The table is divided into four columns: first year, sophomore year, junior year, and senior year. There is also a checklist on the right that lists all of the requirements for the major. Once the student selects their first course, the table updates to show next potential courses for the major. The checklist will also update and mark the course as completed.


## Deployment

*Project Status:* This site is currently designed for Computer Science majors to map out their major requirements. Future steps include incorporating all majors and general distribution requirements.

## Built With

* [Bootstrap](https://getbootstrap.com/) - Front-end component library
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - Extension for Flask

## Presentation
See our beautiful presentation [here](https://docs.google.com/presentation/d/1PjIZG-pibjpCQITDE-zyxkUG_wh3TNCkFltHtgoQ6kI/edit?usp=sharing)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thank you to anyone whose code was used
* The 2019 Hackathon for bringing us together
* And Shayna Nickel for reassuring us that this was an *okay* idea
