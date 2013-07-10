
Intersection Collision Evaluation (ICE)
====================
####GitHub: https://github.com/mainecivichackday/crashreport
####Prezi: http://prezi.com/trnojsgvyznw/?utm_campaign=share&utm_medium=copy

Description
-----
Accidents happen. Car accidents cost money, time, and most importantly lives. Our mission was to take car accident data from the state of Maine over the 2009-2011 period and see what analysis could be done with it.

We built an interactive map of the crash data using Google Maps APIs and the data from the state of maine. We used a RIAK database to store the data and then Python and Javascript to pull the data and display it on our interactive map. Using CSS we created pull out menus which display more data about the crash location or allow the user to restrict what accident sites are seen on the map. The restrictions can be limited by the number of crashes per location, year, or crash reduction factors.

Looking to the future we built a form for submitting accidents to the dataset. This addition includes location, date, time, fatalities, and more. If a city submits their crash data as the accidents are reported it would show which areas are improving, which areas could use improvement, and track improvement over the years.

Our hope is that cities and towns will use our project to cut down on car accidents saving time, money, and lives.

Software
--------

  * Riak Database
  * Python
  * JavaScript
  * Google Maps API v3.
  * CSS
  * jQuery

Contact
-----
####Members:
  * Yuval Boss yuval@yuvalboss.com
  * Andrew Pellett anrope@gmail.com
  * Ryan Jones waker225@gmail.com
  * Trevor Metivier TrevorMetivier@gmail.com
  * Sarah Morehead sarah.morehead@maine.edu
  * Zack Schiller zacheryschiller@gmail.com

License
-------
The MIT License (MIT)

Copyright (c) 2013 Maine Hacker Club

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
