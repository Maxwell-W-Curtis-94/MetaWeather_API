import requests
from concurrent.futures import ThreadPoolExecutor

THREAD_COUNT = 3
URLS = {
    'Salt Lake Cit': 'https://www.metaweather.com/api/location/2487610/',
    'Los Angeles': 'https://www.metaweather.com/api/location/2442047/',
    'Boise': 'https://www.metaweather.com/api/location/2366355/',
}


def output(name, avg_temp):
    """
    Simple output function

    :param name: The name of the city.
    :param avg_temp: The average temperature of the city.
    :return:N/A
    """
    print(f'{name} Average Max Temp: {avg_temp}')


def task(names, url):
    """
    Requests the weather API, collects the max_temp(s)for the url then averages the value.
    :param names: Name of the city.
    :param url: The weather URL
    :return:N/A
    """
    r = requests.get(url=url)
    try:
        data = [max_temp['max_temp'] for max_temp in r.json()['consolidated_weather']]
        output(names, sum(data) / len(data))
    except KeyError as err:
        print(err)


def run():
    """
    Runner function
    Creates THREAD_COUNT threads
    Loops over the dict of URLS
    :return:N/A
    """
    executor = ThreadPoolExecutor(THREAD_COUNT)
    for names, url in URLS.items():
        executor.submit(task, names, url)


if __name__ == '__main__':
    run()
