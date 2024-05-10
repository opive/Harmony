def calculate_similarity(artist_list1, artist_list2):
    set1 = set(artist_list1)
    set2 = set(artist_list2)
    
    # Calculate the number of common artists
    common_artists_count = len(set1.intersection(set2))
    
    # Calculate the similarity score as a percentage of common artists
    similarity_score = (common_artists_count / len(set1.union(set2))) * 100
    
    return similarity_score

# Example artist lists for two users
user1_artists = ['artist1', 'artist2', 'artist3', 'artist4', 'artist5']
user2_artists = ['artist2', 'artist3', 'artist6', 'artist7', 'artist8']

# Calculate the similarity score
similarity_score = calculate_similarity(user1_artists, user2_artists)
print(f"Similarity score: {similarity_score}%")
