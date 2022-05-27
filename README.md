A Search Engine to hunt DSA problems from Codeforces, Codechef and Leetcode.

The app is hosted on https://desearch.herokuapp.com/      **[Note: Please do not query over there, the app will break]**


<h2>Installation</h2>
1 Clone the repository </br>

```git clone https://github.com/abhilashdzr/Desearch.git ```</br>

2 Start and activate a virtual env ``` python3 -m venv env ```  ``` source env/bin/activate ``` </br>

3 Install node ```https://nodejs.org/en/download/```

4 Install dependencies
``` pip install -r requirements.txt ```
``` npm install ```

5 Run the server ``` npm start ```</br>

6 Log in to ```localhost:3000```


<h2>POINTS to NOTE when querying</h2>
1. See that the spellings of the words are correct </br>
2. In case none of the typed words are familiar to the database, it will randomly generate 10 results. </br>
3. It might be possible that the question you type in is not present in the database, so might not be retrieved. If you do not get appropriate results, then try adding a few more keywords or correct any spelling mistake, if present </br>
4. This database might show results according to question tags, but will not according to company tags (e.g. Amazon, Microsoft) </br>
5. Any query takes at most 2.5 seconds to load, so hang on for that time  </br>

