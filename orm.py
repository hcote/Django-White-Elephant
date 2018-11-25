# Select all of the artist objects in the database
Artist.objects.all()

# Get the artist with the id of 1 (can also do pk here which stands for primary key)
Artist.objects.get(id=1)

# Get the artist with the name "Sigur Ros", if there are two Sigur Ros's this will error!
Artist.objects.get(name="Sigur Ros")

# Get all the Artists who are from Iceland
Artist.objects.filter(nationality="Iceland")

# Create an Artist with the following attributes, then save, commiting it to the database
sigur_ros = Artist(name="Sigr Ros", photo_url="test.com", nationality="Iceland")
sigur_ros.save()

# Oops, we misspelled Sigur Ros's name! Let's change it and then commit to the DB
sigur_ros.name = "Sigur Ros"
sigur_ros.save()

# Let's add a song to the artist
song = Song(title="Hoppipolla", album="Takk", preview_url="test.com", artist=sigur_ros)
song.save()

# Delete the song
song.delete()