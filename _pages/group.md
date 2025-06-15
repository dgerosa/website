---
layout: archive
title: "Group"
permalink: /group/
author_profile: true
---

<style>
.people-list {
  display: flex;
  flex-direction: column;
  gap: 1.5em;
  margin-top: 2em;
}

.person {
  display: flex;
  align-items: center;
  background-color: #f2f2f2; /* light mode gray */
  padding: 1em;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.person-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 1.5em;
  flex-shrink: 0;
}

.person-text {
  line-height: 1.5;
}

/* Responsive layout */
@media (max-width: 600px) {
  .person {
    flex-direction: column;
    text-align: center;
  }

  .person-photo {
    margin: 0 0 1em 0;
  }
}

/* Dark mode using attribute selector */
html[data-theme="dark"] .person {
  background-color: #5a5a5a !important;
  color: #ddd !important;
}
</style>


{% include base_path %}

{% include_relative _group.md %}

*For group members, more info is on our [internal wiki](https://github.com/dgerosa/group/wiki).*
