from langchain_community.tools.tavily_search import TavilySearchResults

# 创建 TavilySearchResults 实例，设置最大结果数为3
tavily_search = TavilySearchResults(max_results=3)