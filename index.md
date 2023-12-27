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
Welcome to DSC40A Winter 2024! Please note that the weekly schedule below is not final. If you have any question, please feel free to email the instructor.

{{ site.staffersnobio }}

<!-- [Lecture Recordings](https://podcast.ucsd.edu/){: .btn .btn-blue } [Assignment Solutions](https://campuswire.com/c/GAA3B3FEA/feed/17){: .btn .btn-purple } -->

{% for module in site.modules %}
{{ module }}
{% endfor %}
