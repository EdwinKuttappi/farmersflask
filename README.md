## APCSP [RECS Project](https://github.com/raunak2007/RECS-repo) Backend
The backend consists of four databases and APIs for each separate frontend project created by each group member. 

### Destinations around the world - Colin's feature

Supports get, post, delete, and put(only for likes, which is represented by image URL)

- "title": 2 to 30 character string meant to represent a destination around the world, submitted by users on the frontend
- "text": 2 to 800 character review of said destination, also submitted by users on the frontend
- "imageURL": Not actually an image, I changed it far into development - might fix it later if I have time. Holds an integer to represent a like count for each post

### Find Maps for Location - Edwin's Feature
- "title": 

NOTE: Put functions abnormally. You can only change imageURL/likes and whatever int is inputted changes the likes rather than set them for ease of development on the frontend
