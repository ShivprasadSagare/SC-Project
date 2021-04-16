pip3 install -r requirements.txt -> Installs the required packages to run the app
python3 app.py -> Starts the server
Go to http://0.0.0.0:5000 to view the web app
(Shivprasad and Swayatta) -> Select politicians from the dropdown and click on go 
(Meghana) -> Select actors from the dropdown and click on go 
You can now start creating the test dataset.

Select as many relevant triples as possible.
If there are no relevant triples or only a few relevant triples or if the sentence is very small, do not select anything and just click submit. The data won't be stored and a new sentence appears.
Sometimes, the person's name is shown as some Q-id, for example Q3567879. Ignore such sentences and move on.
The results are stored in testP.json for politicians and testA.json for actors in the same directory as app.py.
You can check how many sentences you have annotated by running "grep 'entity_id' testP.json | wc -l" for politicians and  "grep 'entity_id' testA.json | wc -l" for actors.
In case you are exiting the app before finishing your quota of 100 sentences, make sure to note the entity number till which you have annotated. It is visible in the web page at the top. This makes it easier for you to continue from where you left off.
Get back to me if there are any doubts.
Sorry for not being able to deploy it :(