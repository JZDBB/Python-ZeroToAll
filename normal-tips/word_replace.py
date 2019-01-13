from flashtext import KeywordProcessor

# found keywords
keyword_processor = KeywordProcessor()
# keyword_processor.add_keyword(<unclean name>, <standardised name>)
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('I love Big Apple and Bay Area.')
print(keywords_found)

# replace keywords
keyword_processor1 = KeywordProcessor()
keyword_processor1.add_keyword('New Delhi', 'NCR region')
new_sentence = keyword_processor1.replace_keywords('I love Big Apple and new delhi.')
print(new_sentence)

# 区分大小写
keyword_processor2 = KeywordProcessor(case_sensitive=True)
keyword_processor2.add_keyword('Big Apple', 'New York')
keyword_processor2.add_keyword('Bay Area')
keywords_found = keyword_processor2.extract_keywords('I love big Apple and Bay Area.')
print(keywords_found)

# 提取关键字范围
keyword_processor3 = KeywordProcessor()
keyword_processor3.add_keyword('Big Apple', 'New York')
keyword_processor3.add_keyword('Bay Area')
keywords_found = keyword_processor3.extract_keywords('I love big Apple and Bay Area.', span_info=True)
print(keywords_found)

# 额外信息
kp = KeywordProcessor()
kp.add_keyword('Taj Mahal', ('Monument', 'Taj Mahal'))
kp.add_keyword('Delhi', ('Location', 'Delhi'))
print(kp.extract_keywords('Taj Mahal is in Delhi.'))