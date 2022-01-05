import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
themonths={'1':'january',
            '2':'february',
            '3':'march',
            '4':'april',
            '5':'may',
            '6':'june'}
days_of_week={'1':'monday',
            '2':'teusday',
            '3':'wednesday',
            '4':'thursday',
            '5':'friday',
            '6':'saturday',
            '7':'sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city=input("please enter the city to filter by (u can enter all for ): ")
        if city.lower()=='end':
            print('closing....')
            break
        elif city.lower() not in CITY_DATA:
            print('wrong input please try again')
            continue

        else:
            print('the city u selected is {}'.format(city.title()))
            break




    # get user input for month (all, january, february, ... , june)
    while True :
        month=input('please enter month')
        if month in themonths.keys():
            print('u have choosen{}'.format(themonths[month]))
            month=int(month)
            break
        elif (month.lower() in themonths.values()):
            print('u have choosen{}'.format(month.title()))
            months=['january', 'february', 'march', 'april', 'may', 'june']
            month=months.index(month.lower())+1
            break
        elif month=='all':
            print('you selected not to filter by the months .....')
            break

        else:
            print('Wrong entry please select valid month ')
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day=input('please enter day of the week')
        if day in days_of_week.keys():
            print('u have choosen{}'.format(days_of_week[month]))
            break
        elif (day.lower() in days_of_week.values()):
            print('u have choosen{}'.format(day.title()))
            break
        elif day=='all':
            print('you selected not to filter by day')
            break

        else:
            print('Wrong entry please select valid day ')
            continue

    print('-'*40)
    return city.lower(), month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        df=pd.read_csv(CITY_DATA[city])
    except:
        print('we can not find the file you are searching for please check it and rerun the program')
        print('the data file should be in the same directory with the program')
        input('just press enter to close the program')
        quit()
    df['Start Time']=pd.to_datetime(df['Start Time'])
    print(df.head())
    df['month']=df['Start Time'].dt.month
    print(df.head())
    df['day_of_week']=df['Start Time'].dt.day_name()
    print(df.head())
    if month=='all':
        print('you selected all the months')
    else:
        df=df[df['month']==month]
    print(df.head())
    if day=='all':
        print('you selected all the week days')
    else:
        df=df[df['day_of_week']==day.title()]
    print(df.head())
    print(df.describe())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most frequent month = {}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('the most frequent day of week ={}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('the most common start time = {}'.format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most commonly used start station is {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('the most commonly used end station is {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('the most frequent combination is {}'.format((df['Start Station']+' to '+df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_duration=df['Trip Duration'].sum()
    minuts,seconds=divmod(total_duration,60)
    hour,minuts=divmod(minuts,60)
    print('the total travel time is {} hours,{} minuts,{} seconds'.format(int(hour),int(minuts),int(seconds)))


    # display mean travel time
    mean_tavel_time=df['Trip Duration'].mean()
    minuts,seconds=divmod(mean_tavel_time,60)
    hour,minuts=divmod(minuts,60)
    if minuts==0 and hour==0:
        print('the avgrage travel time is {} seconds'.format(int(seconds)))
    elif hour==0:
         print('the avgrage travel time is  {} minuts and {} seconds'.format(int(minuts),int(seconds)))
    else:
        print('the avgrage travel time is {} hours {} minuts and {} seconds'.format(int(hour),int(minuts),int(seconds)))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('the user types and thier counts are as follow : \n {}'.format(df['User Type'].value_counts()))

    # Display counts of gender
    try:
        print('the users gender and thier counts are as follow : \n {}'.format(df['Gender'].value_counts()))
    except:
        print('there is no gender column in this data set')
    # Display earliest, most recent, and most common year of birth
    try:
        print('the earliest date of birth is {}'.format(int(df['Birth Year'].min())))
        print('the most recent date of birth is {}'.format(int(df['Birth Year'].max())))
        print('the most common date of birth is {}'.format(df['Birth Year'].mode()[0]))
    except:
        print('there is no Birth year column in this dataset')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def data_display(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        data frame
    Returns:
        none
    '''
    rows_to_show=5 ##number of rows that will be shown at every time
    start=0 ##the starting row
    end=rows_to_show-1 ##last row to display
    want_to_see=input('would you like to see some row data')
    while True:
        if want_to_see.lower() not in['yes','no']: ##checking for a valid input
            want_to_see=input('wrong input please enter yes or no')
            continue
        if want_to_see.lower() == 'no':
            break
        elif want_to_see.lower()=='yes':
            print('displaying rows 1 to 5........')
            print(df.iloc[start:end+1])
            start+=rows_to_show
            end+=rows_to_show
            want=input('would you like to see more 5 columns ?')
            while True:
                if want.lower() not in['yes','no']: ##checking for a valid input
                    want=input('wrong input please enter yes or no')
                    continue
                if want=='yes':
                    print('displaying rows {} to {}........'.format(start+1,end+1))
                    print(df.iloc[start:end+1])
                    want=input('would you like to see more 5 columns ?')
                    while True:
                        if want.lower() not in ['yes','no']:
                            want=input('wrong input please enter yes or no')
                            continue
                        else:
                            break
                    start+=rows_to_show
                    end+=rows_to_show
                if want=='no':
                    want_to_see='no'
                    break

def main():
    print('starting.....')
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)
        data_display(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
