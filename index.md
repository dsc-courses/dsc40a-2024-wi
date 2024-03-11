---
layout: home
title: Home
nav_exclude: false
nav_order: 1
seo:
  type: Course
  name: Just the Class
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{: .note }
Midterm 2 Seat has been posted, please find it [Here](resources/lecture/midterm2_seat.pdf). This time it is sorted in alphabetical order of your first name. If you could not find your name in the seating chart, please wait near the podium similar to last time.

{{ site.staffersnobio }}

<!-- [Lecture Recordings](https://podcast.ucsd.edu/){: .btn .btn-blue } [Assignment Solutions](https://campuswire.com/c/GAA3B3FEA/feed/17){: .btn .btn-purple } -->

{% for module in site.modules %}
{{ module }}
{% endfor %}
