# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 02:01:42 2016

@author: jmeza

This code is meant to help restructure how Reduce_Spec.py will read list
and how it will form names. This code is meant to be used along with the list 
out of the "ZZCeti_Test_Data" directory. 

Goals):
- read and parce out multiple flats / stars / standards out of a single list.
- take names from the images themselves, not the list names.
- be able to tell if ther is a problem with the list. 
- Eventualy this code will be merged with Reduce_Spec.py

list Inputs: 

listZeros
listFlats
listStars
listStands

"""
# Imports ====================================================================


# Functions ==================================================================

def Read_List( lst ):
    # This function reads a list of images and decomposes them into a python
    # list of image names. 
    list_file = open(lst,'r')
    im_list = list_file.read()
    list_file.close()
    im_list = im_list.split()
    return im_list    
    
def List_Combe(img_list):
    # This is meant to combe trough list names to identify seperate
    # stars / flats / standars 

    sub_lists= [] # list of sub_list of images 
    sl= [] # sub_list of images
    sl.append(img_list[0]) # place first image in sublist
    
    i= 0; # image counter  
    while i < len(img_list)-1: # run trough all images 
        if img_list[i+1].__contains__(img_list[i][4:]) == True:
            sl.append(img_list[i+1]) # place it in the sub_list 
        else:
            # if the images dont match: 
            sub_lists.append(sl) # write the sublist to the list of sublist 
            sl= [] # clear the sublist
            sl.append(img_list[i+1]) # append the image to the new list 
        i= i+1 # image counter
    sub_lists.append(sl) # append the last sublist to the list of sublist 
    return sub_lists # return the list of sub_list of images


# Code ======================================================================

# Read list and turn them into a python list of names #

zero_lists = List_Combe( Read_List( 'listZeros' ) )
flat_lists = List_Combe( Read_List( 'listFlats' ) )
star_lists = List_Combe( Read_List( 'listStars' ) )
stand_list= List_Combe( Read_List('listStands') )

name_zero= zero_lists[0][0][5:]
print (name_zero)

i= 0;
for flat in flat_lists:
    name_flat= flat[0][5:]
    print(name_flat)
    
for star in star_lists:
    name_star= star[0][5:]
    print(name_star)
    
for stand in stand_list:
    name_stand= stand[0][5:]
    print(name_stand)

print(flat_lists)
print(star_lists)





