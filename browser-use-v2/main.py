from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

browser = Browser(
	config=BrowserConfig(
		headless=True,
	)
)

async def main():
    model = ChatDeepSeek(
        model="deepseek-chat",
    )
    # model = ChatOpenAI(
    #     model="gpt-4o-mini",
    # )
    agent = Agent(
        task="""
あなたは価格監視のエージェントです。
与えられたURLから最新商品の詳細ページに遷移して後述する項目を取得してください。
- cando netshop url: https://netshop.cando-web.co.jp/view/category/all_items

詳細ページから取得する項目
- 価格(price)
- 送料(shipping_fee)
- JANコード(jan_code)
- 本体サイズ(body_size)
- 詳細ページのURL(detail_url)

その他の仕様
- 上記の項目が見つからない場合は-を返してください。
- 取得したデータはcsv形式で出力してください。
""",
        llm=model,
        browser=browser,
    )
    result = await agent.run()
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
