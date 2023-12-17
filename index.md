---
layout: home
title: Home
nav_exclude: false
nav_order: 1
seo:
  type: Course
  name: Just the Class
---

# {{ site.tagline }} 🥑
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{: .note }
[🪑 Seating assignments](resources/exams/seating_final.pdf) for the final exam are now posted. Note that our final is in Center 115, not our regular classroom!  Also, if at least 85% of the class fills out both the [End of Quarter Survey](https://forms.gle/RLSFGKLVsmwtftncA) and [SETs (Student Evaluations of Teaching)](https://academicaffairs.ucsd.edu/Modules/Evals), we will add 0.5% of extra credit to everyone's overall grade. The deadline to complete both surveys is **Saturday, June 10 at 9AM**.

{{ site.staffersnobio }}

[Lecture Recordings](https://podcast.ucsd.edu/){: .btn .btn-blue } [Assignment Solutions](https://campuswire.com/c/GAA3B3FEA/feed/17){: .btn .btn-purple }

{% for module in site.modules %}
{{ module }}
{% endfor %}
