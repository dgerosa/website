---
title: "Fun project: automatic seminar reminders"
date: 2026-07-13
permalink: /posts/2026-07-13-fun-project-automatic-seminar-reminders
tags:
  - Milano
---

I recently had some fun setting up a bot that sends automatic reminders for our group seminars (if you've ever done it, you know that remembering to send seminar emails is a pain). Let me share it here in case it is useful to others:

[github.com/dgerosa/astroseminars_bicocca](https://github.com/dgerosa/astroseminars_bicocca)

Some of the things I learned:

- My goal was to have a single entry point where people organizing seminars can add their speakers, and then everything else is handled automatically. I set this up using [a shared group calendar](https://calendar.google.com/calendar/embed?src=9csetts22iqc0iduial5obme3g%40group.calendar.google.com&ctz=Europe%2FRome).
- The script fetches data from the calendar and sends emails. It turns out that the easiest way to send emails is to set up a dedicated Gmail account; ours is called `astrobicocca.bot@gmail.com`. You also need to generate what Google calls an "app password," which is different from the full Google account password.
- The code runs via a GitHub Action, with that password inserted a GitHub secret
- For running this automatically, it turns out scheduled (cron) GitHub Actions are not always reliable, so I use our computing system, [redfive](posts/2026-05-01-redfive-standing-by), to trigger the GitHub Action itself. If anyone has a better solution, please let me know!

The system has now been deployed for a few months, and it has been working very well. Every Friday, it sends a summary of the following week's events, and on seminar days it sends a reminder early in the morning.