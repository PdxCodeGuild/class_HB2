## Name

myJaxn

## Project Overview

Project will be focused on an app that allows users to enter information focused on the municipality of Jackson in the state of Mississippi.  Data will range from infrastructure issues to community based orgs and events.  Jackson has had a wealth of significant issues relating to infrastructure including a failing public water system, transportation, road management and displaced citizens.  What I envision is a data hub that allows citizens to submit user data to the site with issues that they are experiencing first hand.  I would also like to include highlights of the commnity that users can also enter to make information readily available to the public. These could be commnity based gatherings and festivals or after hour youth development programs, to courts where pick-up games are played frequently.  I would like to include a map overlay of the city that will display clickable icons with events and issues being rendered and a searchable data base.

## Walk through the application from the user's perspective. What will they see on each page? What can they input and click and see? How will their actions correspond to events on the back-end?

User will initially see a welcome page that will point them in several directions. They will be able to search for events by keyword, or view a map of all events listed currently.  They can also be directed to a path that will allow them to report data to the site.  This data entry will allow the user to select various entries ranging from incidents, events or other.  I would like to allow users to create events and or incidents and have it pend in the system awaiting admin approval after review.

## Data Model

User models will exist for admin functions.  I may create a user login form that will allow a user to view past account information or maybe a system to verify and upgrade a user to different tier levels for site uploads bypassing admin approvals.  That would be a latter milestone feature however.

Models will be seperated into a couple categories.  One will be incident related that represents an issue or problem, this could be water pressure low at this address to pots holes located on this road.  This will put incidents in models seperate then those deemed commnity based events.  Another model would be designated for those.  This will allow users to search community events and projects seperately.  Fields are going to range from model to model but generally they will include location, description, date with optional features such as file uploads for fliers or pictures taken of incidents.


## Schedule

Milestone 1 - Framework built with functioning  base models and database.  URLS functioning properly with templates at most pages.  Anticipated time - Week 1
Milestone 2 - Working map and data entry to said feature.  Aniticipated timeframe - Week 2
Milestone 3 - Fully functioning URLS and map feature, user entry data processing and rendering into database properly.  Admin and user login management system implemented. Anticipated timeframe - Week 3
