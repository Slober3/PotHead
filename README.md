# PotHead

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0ae093f1196d4b6eb9d7a4d7a0aa9e07)](https://www.codacy.com/app/quintendesmyter/PotHead?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Slober3/PotHead&amp;utm_campaign=Badge_Grade)

## What is it?
Pothead: A simple lightweight packet for creating a minimal interaction honeypot


## How does it work?
Magic, Well kinda you don't need super dupper knowledge to use this!
Oops the magic failed ;) a really nice INSTALL.md will be written unfortunately it's not yet available.
1) Download all the files 

2) Check if you got everything

3) Upload and configure the Website and backend (includes/Config.php & the .SQL files)

4) Do not forget to change your APIKEY!

5) Run the python file!

```
Pothead.py -pp 22 23 -site http://YOURSITE.COM/api/write.php -apikey YOURAPIKEY
```

6) Profit!

## Is this for anyone?
Hmmmm, yes and no I would suggest you know a thing or two about PHP & Python. 
It's a pre-release and still in the early alpha stage.

## Is it safe?
It's pretty safe ;)

## Does it work?
Yeah check it live!
1) View the last few connections (_OLD): http://7ol.eu/view.php

2) View the last few inputs (_OLD): http://7ol.eu/inputView.php

3) The new API interface: http://7ol.eu/


## API

The API is working! It's still running on fossil fuels and is currently beining updated to run on solar!
```
Formatted JSON Data
[  
   {  
      "id":"1238",
      "ip":"59.45.175.86",
      "time":"2017-07-05 02:18:17",
      "port":"22",
      "portHacker":"43045"
   }
]
```

## Contributors
We are still searching brainstormers, users who would like to help and guys who would love to dive into this awesome project.

## Contact
1) Hackforums username: slober

2) Email: pothead@7ol.eu

## Screenshot

![example](http://i.imgur.com/w7cLe2Q.jpg)

## License
This projects is Licensed under the MIT license.
