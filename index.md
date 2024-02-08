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
Midterm 1 will be on Friday, Feb. 9th. The [Assigned Seat](resources/exams/seating_mdtm1.pdf) is posted. If you could not find your student ID on this file, please come to the podium and talk to me before the exam start, I will assign a seat to you.

{{ site.staffersnobio }}

<!-- [Lecture Recordings](https://podcast.ucsd.edu/){: .btn .btn-blue } [Assignment Solutions](https://campuswire.com/c/GAA3B3FEA/feed/17){: .btn .btn-purple } -->

{% for module in site.modules %}
{{ module }}
{% endfor %}
