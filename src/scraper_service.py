from matrx_utils.socket.core.service_base import SocketServiceBase
from dataclasses import asdict
from matrx_utils.database.orm.manager import ScrapeDomainManager

verbose = False

success_search_sample = {
    "response_type": "search_results",
    "metadata": {
        "keyword": "giorgia meloni trump"
    },
    "results": [
        {
            "keyword": "giorgia meloni trump",
            "type": "news",
            "title": "Giorgia Meloni whispers soothing words to Trump on ‘western nationalism’ | The Guardian",
            "url": "https://www.theguardian.com/us-news/2025/apr/17/giorgia-meloni-trump-meeting",
            "description": "The president and Italy’s prime minister spoke a common language – but for a discordant moment over Ukraine.",
            "source": "The Guardian",
            "age": "3 days ago",
            "thumbnail": "https://i.guim.co.uk/img/media/4fd653093a69d16d4d3e0575979111597f8f2c4c/0_224_4539_2723/master/4539.jpg?width=1200&height=630"
        },
        {
            "keyword": "giorgia meloni trump",
            "type": "web",
            "title": "Meloni and Trump: A Meeting of Minds? | BBC",
            "url": "https://www.bbc.com/news/world-us-europe-12345678",
            "description": "Italian PM Giorgia Meloni meets US President Trump to discuss trade and nationalism.",
            "source": "BBC",
            "age": "4 days ago",
            "thumbnail": None
        }
    ]
}

sample_successful_scrapes = data = {
    "response_type": "scraped_pages",
    "metadata": {
        "execution_time_ms": 2500
    },
    "results": [
        {
            "status": "success",
            "url": "https://www.theguardian.com/us-news/2025/apr/17/giorgia-meloni-trump-meeting",
            "error": None,
            "overview": {
                "uuid": "a2b3c4d5-e6f7-8901-bcde-1234567890ab",
                "website": "theguardian.com",
                "url": "https://www.theguardian.com/us-news/2025/apr/17/giorgia-meloni-trump-meeting",
                "unique_page_name": "www_theguardian_com_us_news_2025_apr_17_giorgia_meloni_trump_meeting",
                "page_title": "Giorgia Meloni whispers soothing words to Trump on ‘western nationalism’ | The Guardian",
                "has_structured_content": True,
                "table_count": 0,
                "code_block_count": 0,
                "list_count": 2,
                "outline": {
                    "H1: Giorgia Meloni whispers soothing words to Trump on ‘western nationalism’": [],
                    "H2: Diplomatic Highlights": [],
                    "H2: Related Topics": [],
                    "unassociated": []
                },
                "char_count": 6100,
                "char_count_formatted": 7200,
                "metadata": {
                    "json-ld": [],
                    "opengraph": {},
                    "meta_tags": {
                        "description": "The president and Italy’s prime minister spoke a common language – but for a discordant moment over Ukraine",
                        "viewport": "width=device-width,minimum-scale=1,initial-scale=1",
                        "article:author": "https://www.theguardian.com/profile/roberttait",
                        "article:published_time": "2025-04-17T21:51:15.000Z",
                        "article:modified_time": "2025-04-17T22:29:26.000Z"
                    },
                    "canonical_url": "https://www.theguardian.com/us-news/2025/apr/17/giorgia-meloni-trump-meeting",
                    "robots_directives": "max-image-preview:large"
                }
            },
            "structured_data": {
                "Ordered Lists": {
                    "H1: Giorgia Meloni whispers soothing words to Trump on ‘western nationalism’": [
                        {
                            "Before": "",
                            "List": [
                                "[Donald Trump](https://www.theguardian.com/us-news/donaldtrump)",
                                "[Giorgia Meloni](https://www.theguardian.com/world/giorgia-meloni)",
                                "[Italy](https://www.theguardian.com/world/italy)",
                                "[US politics](https://www.theguardian.com/us-news/us-politics)"
                            ],
                            "After": ""
                        }
                    ]
                }
            },
            "organized_data": {
                "H1: Giorgia Meloni whispers soothing words to Trump on ‘western nationalism’": [
                    "The president and Italy’s prime minister spoke a common language – but for a discordant moment over Ukraine",
                    "She had been welcomed to the White House with open arms as few other foreign visitors had been since Donald Trump’s return.",
                    "Italy’s prime minister, whose Brothers of Italy party has roots in neo-fascism, emphasized shared values."
                ],
                "H2: Diplomatic Highlights": [
                    "Meloni introduced the concept of ‘western nationalism’ to bridge transatlantic differences.",
                    "A question about Ukraine revealed tensions, with Trump distancing himself from Zelenskyy."
                ]
            },
            "text_data": "Giorgia Meloni whispers soothing words to Trump on ‘western nationalism’\n\nThe president and Italy’s prime minister spoke a common language – but for a discordant moment over Ukraine\n\nShe had been welcomed to the White House with open arms as few other foreign visitors had been since Donald Trump’s return, and Giorgia Meloni wanted to assure her host that – at least when it came to their political worldview – they spoke a common language.\n\nItaly’s prime minister, whose Brothers of Italy party has roots in neo-fascism, was keen to stress shared values...",
            "main_image": "https://i.guim.co.uk/img/media/4fd653093a69d16d4d3e0575979111597f8f2c4c/0_224_4539_2723/master/4539.jpg?width=1200&height=630&quality=85&auto=format&fit=crop",
            "hashes": [
                "sha256:def456ghi789",
                "md5:jkl012mno345"
            ],
            "content_filter_removal_details": [
                {
                    "attribute": "tag",
                    "match_type": "exact",
                    "trigger_value": "aside",
                    "text": "Promotional sidebar content",
                    "html_length": 400
                },
                {
                    "attribute": "class",
                    "match_type": "partial",
                    "trigger_value": "ad-banner",
                    "text": "Advertisement",
                    "html_length": 200
                },
                {
                    "attribute": "tag",
                    "match_type": "exact",
                    "trigger_value": "footer",
                    "text": "Newsletter signup",
                    "html_length": 1200
                }
            ],
            "links": {
                "internal": [
                    "https://www.theguardian.com/us-news/donaldtrump",
                    "https://www.theguardian.com/world/giorgia-meloni",
                    "https://www.theguardian.com/world/italy",
                    "https://www.theguardian.com/us-news/us-politics"
                ],
                "external": [
                    "https://www.bbc.com/news/articles/cg5q0mev07lo",
                    "https://www.facebook.com/theguardian",
                    "https://twitter.com/guardian"
                ],
                "images": [
                    "https://i.guim.co.uk/img/media/4fd653093a69d16d4d3e0575979111597f8f2c4c/0_224_4539_2723/master/4539.jpg?width=1200&height=630",
                    "https://i.guim.co.uk/img/media/4fd653093a69d16d4d3e0575979111597f8f2c4c/0_224_4539_2723/master/4539.jpg?width=465&dpr=1"
                ],
                "documents": [
                    "https://uploads.guim.co.uk/2024/08/27/TAX_STRATEGY_2025.pdf"
                ],
                "others": [
                    "mailto:?subject=Giorgia Meloni whispers soothing words to Trump&body=https://www.theguardian.com/us-news/2025/apr/17/giorgia-meloni-trump-meeting"
                ],
                "audio": [],
                "videos": [],
                "archives": []
            }
        },
        {
            "status": "error",
            "url": "https://www.bbc.com/news/world-us-europe-12345678",
            "error": "HTTP 403 Forbidden",
            "overview": None,
            "structured_data": None,
            "organized_data": None,
            "text_data": None,
            "main_image": None,
            "hashes": None,
            "content_filter_removal_details": None,
            "links": None
        }
    ]
}

sample_search_failure = {
    "error_type": "search_error",
    "message": "Error processing keyword 'artificial intelligence'. Exception: HTTP 429: Too Many Requests from Brave Search API",
    "details": {
        "keyword": "artificial intelligence",
        "traceback": (
            "Traceback (most recent call last):\n"
            "  File \"/app/scraper/api_management/brave_search/search_async.py\", line 52, in async_brave_search\n"
            "    response = await client.get(url, headers=headers, params=params, timeout=timeout)\n"
            "  File \"/usr/lib/python3.9/httpx/_client.py\", line 1234, in get\n"
            "    response = await self.request('GET', url, **kwargs)\n"
            "  File \"/usr/lib/python3.9/httpx/_client.py\", line 1567, in request\n"
            "    return await self.send(request, **kwargs)\n"
            "  File \"/usr/lib/python3.9/httpx/_client.py\", line 1652, in send\n"
            "    raise HTTPStatusError(response=response, message=message)\n"
            "httpx.HTTPStatusError: HTTP 429: Too Many Requests from Brave Search API"
        )
    },
    "user_visible_message": "Error searching keyword : 'artificial intelligence'"
}

sample_scrape_failure = {
    "error_type": "scrape_error",
    "message": "Failed to scrape URLs due to HTTP 429: Too Many Requests from target site",
    "user_visible_message": "An error occurred while reading pages."
}


class ScrapeService(SocketServiceBase):
    _initialized = False

    def __init__(
            self,
            stream_handler=None,
    ):
        self.keyword = None
        self.max_page_read = None
        self.keywords = None
        self.country_code = None
        self.total_results_per_keyword = None
        self.search_type = None

        self.mic_check_message = None
        self.stream = None
        self.urls = None
        self.stream_handler = stream_handler

        # Additional parameters
        self.get_content_filter_removal_details = None
        self.get_links = None
        self.get_main_image = None
        self.get_text_data = None
        self.get_organized_data = None
        self.get_structured_data = None
        self.get_overview = None
        self.include_highlighting_markers = None
        self.include_media = None
        self.include_media_links = None
        self.include_media_description = None
        self.include_anchors = None
        self.anchor_size = None

    async def process_task(self, task, task_context=None, process=True):
        return await self.execute_task(task, task_context, process)


    async def quick_scrape(self):
        manager = ScrapeDomainManager()
        objects = await manager.load_items()
        await self.stream_handler.send_data_final([obj.to_dict() for obj in objects])


    async def mic_check(self):
        if self.stream_handler:
            await self.stream_handler.send_chunk("Simulating task: search_and_scrape")

            await self.stream_handler.send_status_update(status="processing",
                                                         system_message=f'Searching for "artificial intelligence"',
                                                         user_visible_message=f'Searching for "artificial intelligence"')

            await self.stream_handler.send_data(success_search_sample)

            await self.stream_handler.send_status_update(status="processing",
                                                         system_message=f"Scraping 2 results",
                                                         user_visible_message="Reading pages...")

            await self.stream_handler.send_data(sample_successful_scrapes)

            await self.stream_handler.send_chunk("Testing failure for feature: search")
            await self.stream_handler.send_error(**sample_search_failure)

            await self.stream_handler.send_chunk("Testing failure for feature: scrape")
            await self.stream_handler.send_error(**sample_scrape_failure)

            await self.stream_handler.send_end()
