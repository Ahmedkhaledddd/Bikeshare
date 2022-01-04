import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york city','washington']
    flag=True
    while flag:
        city=input('please enter the city name:')
        city=city.lower()
        if city.lower() in cities:
            print('Thanks, you entered a valid city')
            flag=False
        else:
            print('you enter an invalid city!')
            
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('please enter the month:').lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('please enter the day:').lower()
    
    print('-'*40)
    return city, month, day


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
    CITY_PATH={'chicago':'chicago.csv',
               'new york city':'new_york_city.csv',
               'washington':'washington.csv'}
    df=pd.read_csv(CITY_PATH[city])
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Months']=df['Start Time'].dt.month
    df['Days']=df['Start Time'].dt.weekday_name
    df['hours']=df['Start Time'].dt.hour
    
    if month!='all':
        months=['january','february','march','april','may','june','july','august','september','october','november','december']
        month=months.index(month)+1
        df=df[df['Months']==month]
        
        
    if day!='all':
        df=df[df['Days']==day.title()]

    return df

def view_data_(df):
   view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
   start_loc = 0
   while view_data=='yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: Enter yes or no").lower()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['Months'].mode()[0]
    print('common month is:',common_month)
    
    # TO DO: display the most common day of week
    common_day=df['Days'].mode()[0]
    print('common day is:',common_day)
    
    # TO DO: display the most common start hour
    common_hour=df['hours'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('commonly used start station is:',common_start_station)
    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('commonly used end station is:',common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    #comb_start_end=df.groupby(['Start Station'])['End Station'].mode()
    comb_start_end_1=df.groupby(['Start Station','End Station'])
    print(comb_start_end_1.size().sort_values(ascending=False).head(1))
    #print(comb_start_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time']=pd.to_datetime(df['End Time'])
    # TO DO: display total travel time
   # for i in len(df['Start Time']):
        #total_time=df['Start Time'][i]-df['End Time'][i]
        #print('total time traveled in trip number {} is: {}'.format(i,total_time))
    total_trip_duration=df['Trip Duration'].sum()
    print('total traveled trip duration is',total_trip_duration)
    
    # TO DO: display mean travel time
    trip_mean=df['Trip Duration'].mean()
    print('Trip mean is',trip_mean)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city.lower() != 'washington':
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year=df['Birth Year'].min()
        print('earliest year of birth is',earliest_year)
        recent_year=df['Birth Year'].max()
        print('most recent year is',recent_year)
        most_common_year=df['Birth Year'].mode()[0]
        print('most common year is',most_common_year)
   
    #print('...')
    print('\n This took %s seconds.'%(time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_data_(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
