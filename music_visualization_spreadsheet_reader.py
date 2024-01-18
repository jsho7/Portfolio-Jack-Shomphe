# This project could not have functioned without the efforts of one Zack Shapiro who created a data converter from last.fm to csv files, furthermore this project relies heavily on data collected from my own personal listening using using the last.fm website.
# thank you so much for checking it out and enjoy -Jack


import csv

csv_file_path = "music_dat_as_of_12.6.23.csv"


def read_spreadsheet(desired_column, lst_name):
    with open(csv_file_path, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if len(row) > desired_column:
                value = row[desired_column]
                lst_name.append(value)
        return lst_name


def unique_value(input_lst, output_lst):
    for artist in input_lst:
        if artist not in output_lst:
            output_lst.append(artist)
    return output_lst


def printable_check(input_lst):
    printablecharlst = set(
        "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
    )
    input_lst = [item for item in input_lst if item in printablecharlst]
    return input_lst


def uniquity_count(input_lst_narrow, input_lst_raw, count_dict, input_type):
    artistno = len(input_lst_narrow)
    print("you listen to", artistno, "unique", input_type, "")
    for item in input_lst_raw:
        if item in input_lst_narrow:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
    output_lst = [count_dict.get(item, 0) for item in input_lst_narrow]
    return count_dict


def list_sorting(input_lst):
    input_lst.sort(key=lambda x: x[1])
    return input_lst


def list_reversal(input_lst):
    new_lst = input_lst[::-1]
    return new_lst


def zipping(time_dat, dat_raw):
    tup1 = time_dat
    tup2 = dat_raw
    x = tuple(zip(tup1, tup2))
    return x


def sorted_nums(paired_lst, output_list):
    for pair in paired_lst:
        output_list.append(pair[1])
    return output_list


def convert_to_percentages(numbers, ouput_list):
    max_number = max(numbers)

    x = [(num / max_number) * 100 for num in numbers]
    ouput_list.append(x)
    return ouput_list


def usable_data_for_display(input_lst, output_lst):
    for i in range(len(input_lst)):
        acc = 0
        x = input_lst[i]
        for j in range(len(x)):
            if acc % 2 == 0:
                output_lst.append(x[0])
            acc += 1


def usable_data_for_display_num(input_lst, output_lst):
    for i in range(len(input_lst)):
        acc = 0
        x = input_lst[i]
        for j in range(len(x)):
            if acc % 2 == 1:
                output_lst.append(x[1])
            acc += 1


def artists():
    raw_data_lst_artists = []
    uniquity_lst_artists_str = []
    artists_dict = {}
    sorted_lst_artists = []
    global lst_paired_artists_correct_order
    lst_paired_artists_correct_order = []
    read_spreadsheet(2, raw_data_lst_artists)
    unique_value(raw_data_lst_artists, uniquity_lst_artists_str)
    # print(raw_data_lst_artists)
    # print(uniquity_lst_artists_str)
    printable_check(uniquity_lst_artists_str)
    uniquity_count(
        uniquity_lst_artists_str, raw_data_lst_artists, artists_dict, "artists"
    )
    paired_lst = list(artists_dict.items())
    # print(paired_lst)
    list_sorting(paired_lst)
    # print(paired_lst)
    lst_paired_artists_correct_order = list_reversal(paired_lst)
    # print(lst_paired_artists_correct_order)


def albums():
    raw_data_lst_albums = []
    uniquity_lst_albums_str = []
    albums_dict = {}
    sorted_lst_albums = []
    global lst_paired_albums_correct_order
    lst_paired_albums_correct_order = []
    read_spreadsheet(4, raw_data_lst_albums)
    unique_value(raw_data_lst_albums, uniquity_lst_albums_str)
    # print(uniquity_lst_albums_str)
    printable_check(uniquity_lst_albums_str)
    uniquity_count(uniquity_lst_albums_str, raw_data_lst_albums, albums_dict, "albums")
    paired_lst = list(albums_dict.items())
    # print(paired_lst)
    list_sorting(paired_lst)
    # print(paired_lst)
    lst_paired_albums_correct_order = list_reversal(paired_lst)
    # print(lst_paired_albums_correct_order)


def tracks():
    raw_data_lst_tracks = []
    uniquity_lst_tracks_str = []
    tracks_dict = {}
    sorted_lst_tracks = []
    global lst_paired_tracks_correct_order
    lst_paired_tracks_correct_order = []
    read_spreadsheet(6, raw_data_lst_tracks)
    unique_value(raw_data_lst_tracks, uniquity_lst_tracks_str)
    # print(uniquity_lst_tracks_str)
    printable_check(uniquity_lst_tracks_str)
    uniquity_count(uniquity_lst_tracks_str, raw_data_lst_tracks, tracks_dict, "tracks")
    paired_lst = list(tracks_dict.items())
    # print(paired_lst)
    list_sorting(paired_lst)
    # print(paired_lst)
    lst_paired_tracks_correct_order = list_reversal(paired_lst)
    # print(lst_paired_tracks_correct_order)


def math():
    global percent_dat_artist, percent_dat_album, percent_dat_track, lst_paired_tracks_correct_order, lst_paired_albums_correct_order, lst_paired_artists_correct_order, artist_numbers_only, tracks_numbers_only, albums_numbers_only, tracks_call, albums_call, artists_call, vis_dat_artist, vis_dat_album, vis_dat_track, vis_dat_album_num, vis_dat_artist_num, vis_dat_track_num
    artist_numbers_only = []
    tracks_numbers_only = []
    albums_numbers_only = []

    vis_dat_artist = []
    vis_dat_track = []
    vis_dat_album = []

    vis_dat_track_num = []
    vis_dat_album_num = []
    vis_dat_artist_num = []

    percent_dat_artist = []
    percent_dat_album = []
    percent_dat_track = []

    tracks_call = sorted_nums(lst_paired_tracks_correct_order, tracks_numbers_only)
    # print(tracks_numbers_only)
    albums_call = sorted_nums(lst_paired_albums_correct_order, albums_numbers_only)
    # print(albums_numbers_only)
    artists_call = sorted_nums(lst_paired_artists_correct_order, artist_numbers_only)
    # print(artist_numbers_only)

    convert_to_percentages(tracks_numbers_only, percent_dat_track)
    convert_to_percentages(albums_numbers_only, percent_dat_album)
    convert_to_percentages(artist_numbers_only, percent_dat_artist)

    usable_data_for_display(lst_paired_tracks_correct_order, vis_dat_track)
    usable_data_for_display(lst_paired_albums_correct_order, vis_dat_album)
    usable_data_for_display(lst_paired_artists_correct_order, vis_dat_artist)

    usable_data_for_display_num(lst_paired_tracks_correct_order, vis_dat_track_num)
    usable_data_for_display_num(lst_paired_albums_correct_order, vis_dat_album_num)
    usable_data_for_display_num(lst_paired_artists_correct_order, vis_dat_artist_num)


tracks()
artists()
albums()
math()


def disp(lst_percent, lst_str, lst_num):
    bars(lst_percent)
    making_the_data_not_look_hiddeous(lst_str)
    making_the_data_not_look_hiddeous_num(lst_num)


def bars(input_percent_lst):
    fill_val_lst = [
        (255, 3, 3),
        (245, 20, 20),
        (235, 40, 40),
        (225, 60, 60),
        (215, 80, 80),
        (205, 100, 100),
        (195, 120, 120),
        (185, 140, 140),
        (175, 160, 160),
        (165, 165, 165),
        (165, 190, 190),
    ]
    for i in range(min(10, len(input_percent_lst))):
        percent_value = input_percent_lst[i]
        value = map_range(percent_value, 0, 100, 0, 450)
        x = fill_val_lst[i]
        fill(*x)
        rect(20 + i * 150, 500 - value, 90, value)


def map_range(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))


def making_the_data_not_look_hiddeous(input_lst):
    global vis_dat_track, vis_dat_album, vis_dat_artist
    text_size(15)
    acc = 0
    for i in range(min(10, len(input_lst))):
        value = input_lst[i]
        fill(235, 40, 40)
        text(f"{value}", 20 + i * 150, 515)


def making_the_data_not_look_hiddeous_num(input_lst):
    global vis_dat_track_num, vis_dat_album_num, vis_dat_artist
    text_size(20)
    acc = 0
    for i in range(min(10, len(input_lst))):
        value = input_lst[i]
        fill(235, 40, 40)
        text(f"{value} plays", 20 + i * 150, 530)


def slicing_down(input_lst, output_lst):
    for word in input_lst:
        shortened_word = word[:18]
        output_lst.append(shortened_word)


def mass_slice():
    global sliced_artists, sliced_track, sliced_albums
    sliced_artists = []
    sliced_track = []
    sliced_albums = []

    slicing_down(vis_dat_album, sliced_albums)
    slicing_down(vis_dat_artist, sliced_artists)
    slicing_down(vis_dat_track, sliced_track)


mass_slice()


def setup():
    size(1700, 600)
    global tracks_call, albums_call, artists_call, vis_dat_artist, vis_dat_album, vis_dat_track, vis_dat_album_num, vis_dat_artist_num, vis_dat_track_num


def draw():
    global tracks_call, albums_call, artists_call, vis_dat_artist, vis_dat_album, vis_dat_track, vis_dat_album_num, vis_dat_artist_num, vis_dat_track_num
    background(220, 220, 220)
    key_pressed()


def key_pressed():
    if key == "w":
        clear
        text_size(30)
        text("Tracks data", 10, 30)
        disp(percent_dat_track[0], sliced_track, vis_dat_track_num)
    if key == "a":
        clear
        text_size(30)
        text("Artists data", 10, 30)
        disp(percent_dat_artist[0], sliced_artists, vis_dat_artist_num)
    if key == "d":
        clear
        text_size(30)
        text("Albums data", 10, 30)
        disp(percent_dat_album[0], sliced_albums, vis_dat_album_num)
        
#py5_tools.animated_gif('animatedgifgifgif.gif', 100, 0.05, 0.05) 

