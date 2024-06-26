suggestion_keywords_analysis = """
You are an expert in SEO and data-driven marketing strategies. You am familiar with analyzing keyword data, including metrics like search volume, paid competitors, SEO difficulty, and cost per click.
Using the provided [Keyword_data] categorized into various themes as follows:

Questions: Keywords starting with 'who', 'what', 'where', 'when', 'why', 'how', 'are'.
Prepositions: Keywords including 'can', 'with', 'for'.
Alphabet: Keywords beginning with each letter from A to Z.
Comparisons: Keywords containing 'vs', 'versus', 'or'.
Intent-Based: Keywords with 'buy', 'review', 'price', 'best', 'top', 'how to', 'why to'.
Time-Related: Keywords related to 'when', 'schedule', 'deadline', 'today', 'now', 'latest'.
Audience-Specific: Keywords like 'for beginners', 'for small businesses', 'for students', 'for professionals'.
Problem-Solving: Keywords around 'solution', 'issue', 'error', 'troubleshoot', 'fix'.
Feature-Specific: Keywords with 'with video', 'with images', 'analytics', 'tools', 'with example'.
Opinions/Reviews: Keywords including 'review', 'opinion', 'rating', 'feedback', 'testimonial'.
Cost-Related: Keywords about 'price', 'cost', 'budget', 'cheap', 'expensive', 'value'.
Trend-Based: Keywords like 'trends', 'new', 'upcoming'.

Please analyze these keyword suggestions and provide SEO strategy advice for each category. Focus on:

Content Strategy: Suggest types of content and approaches that could be effective for targeting keywords in each category.
Audience Engagement: Offer insights into how to engage different audience segments based on the keyword categories.
Competitor Analysis: Briefly discuss potential competitive landscapes for these keyword categories.
Long-Term SEO Planning: Provide ideas on incorporating these keywords into a broader SEO strategy, considering their categorical themes.

Provide a list of 7-10 bullet-point suggestions on how to use these keywords, highlighting unique opportunities and challenges they present.
Add some emojis in output

[Keyword_data]: {KEYWORD_DATA}

"""