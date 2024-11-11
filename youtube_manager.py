import json

def load_data():
    try:
        with open('youtube_text.txt', 'r') as file:
            data = json.load(file)
            return [video for video in data if isinstance(video, dict) and 'name' in video and 'time' in video]
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube_text.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n" + "*" * 60)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*" * 60 + "\n")

def add_videos(videos):
    name = input("Enter video name:")
    time = input("Enter video Time:")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter video number whic you want to update:"))
    if 1 <= index <= len(videos):
        name  = input("Enter video name:")
        time = input("Enter video time:")
        videos[index-1] = {'name':name, 'time':time}; 
        save_data_helper(videos)
        print("---- video updated ----")
    else:
        print("Invalid video number")    

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to be deleted:"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("---- video deleted ----")
    else:
        print("Invalid index")

def main():
    videos = load_data()
    while True:
        print("Youtube Manager || Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_all_videos(videos)
        elif choice == 2:
            add_videos(videos)
        elif choice == 3:
            update_videos(videos)
        elif choice == 4:
            delete_videos(videos)
        elif choice == 5:
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
