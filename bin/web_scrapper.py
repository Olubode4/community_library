#!/usr/bin/env python3

import pdb
import time
import mechanicalsoup
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


def scrap_webpage_field():
    """

    :return:
    """
    # url = "http://olympus.realpython.org/profiles/dionysus"
    url = ("https://www.upwork.com/ab/feed/topics/rss?securityToken=46953351ccd263c7200babf4fda8878c96628de5a8c"
                  "7efc006fd6e79099f5b4c3521f2797a0ac06e3ade66b23f95c1f72036f34828a0452440619aca5197eec2&userUid=17362"
                  "65687202025472&orgUid=1736265687202025473&topic=7193631")
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    start_index = html.find("Posted On") + len("Posted On")
    pdb.set_trace()
    end_index = html.find("</h2>")
    title = html[start_index:end_index]
    print(title)
    # pdb.set_trace()
    start_index = html.find("Favorite animal:") + len("Favorite animal:")
    end_index = html[start_index:].find("<")

    title = html[start_index:end_index+start_index]
    print(title)


def scrap_webpage():
    """

    :return:
    """
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)


def scrap_wt_bs4():
    """

    :return:
    """
    # url = "http://olympus.realpython.org/profiles/dionysus"
    url = "http://olympus.realpython.org/dice"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    pdb.set_trace()
    # image_data = soup.find_all("img")
    # image1, image2 = soup.find_all("img")
    pdb.set_trace()
    print(soup.get_text())


def scrap_wt_bs4_two():
    """

    :return:
    """
    url = "http://olympus.realpython.org/profiles"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    # image_data = soup.find_all("img")
    html_data = soup.find_all("a")
    pdb.set_trace()
    link_set = []
    for link in html_data:
        partial_url = link['href']
        link_set.append(f"http://olympus.realpython.org{partial_url}")
    # print(soup.get_text())
    print(link_set)


def scrap_refreshed_page():
    """

    :return:
    """
    browser = mechanicalsoup.Browser()
    url = "http://olympus.realpython.org/dice"
    for i in range(3):
        page = browser.get(url)
        pdb.set_trace()
        tag = page.soup.select("#result")[0]
        result = tag.text
        print(f"The result of your dice roll is: {result}")
        if i < 2:
            time.sleep(5)


def scrap_refreshed_upwork_page():
    """

    :return:
    """
    browser = mechanicalsoup.Browser()
    url = "https://www.upwork.com/nx/find-work/7193631"
    # upwork_url = ("https://www.upwork.com/ab/feed/topics/rss?securityToken=46953351ccd263c7200babf4fda8878c96628de5a8c"
    #               "7efc006fd6e79099f5b4c3521f2797a0ac06e3ade66b23f95c1f72036f34828a0452440619aca5197eec2&userUid=17362"
    #               "65687202025472&orgUid=1736265687202025473&topic=7193631")
    pdb.set_trace()
    for i in range(3):
        page = browser.get(url)
        # pdb.set_trace()
        tag = page.soup.select("Posted On")
        # tag = page.content.select("Posted On")
        pdb.set_trace()
        # tag = page.soup.select("#result")[0]
        # result = tag.text
        # print(f"The result of your dice roll is: {result}")
        # if i < 2:
        #     time.sleep(5)


if __name__ == "__main__":
    # scrap_webpage_field()
    # scrap_webpage()
    # scrap_wt_bs4()
    # scrap_wt_bs4_two()
    # scrap_wt_mec_soup()
    # scrap_refreshed_page()
    scrap_refreshed_upwork_page()