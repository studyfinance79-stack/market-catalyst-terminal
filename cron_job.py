import os
import json
from datetime import datetime

def fetch_live_nse_regulatory_catalysts():
    """
    Simulates parsing raw corporate announcements from the National Stock Exchange.
    Provides clear clean English and translated Hindi text for seamless execution.
    """
    return [
        {
            "company": "Balaji Amines Limited",
            "symbol": "BALAMINES",
            "isin": "INE050E01027",
            "sector": "Specialty Chemicals",
            "category": "QUARTERLY_RESULTS", # Categories include: QUARTERLY_RESULTS, MANAGEMENT_GOVERNANCE, MERGER_DEMERGER, GEOPOLITICAL
            "news_eng": "Official NSE Regulatory Announcement: Stellar Q4 earnings recorded. Core revenue surged by 11.6% Year-on-Year to ₹402.52 Crores. Net Profit After Tax (PAT) expanded exponentially by 60.2% to ₹64.77 Crores, heavily driven by margin tailwinds in aliphatic specialized amides.",
            "news_hin": "आधिकारिक NSE फाइलिंग अपडेट: कंपनी ने शानदार Q4 के नतीजे पेश किए हैं। सालाना आधार (YoY) पर कुल रेवेन्यू 11.6% बढ़कर ₹402.52 करोड़ हो गया है। कंपनी का शुद्ध मुनाफा (PAT) 60.2% की भारी उछाल के साथ ₹64.77 करोड़ दर्ज हुआ है। एलिफैटिक एमाइन सेक्टर में मार्जिन बढ़ने से कंपनी को बड़ा फायदा हुआ है।",
            "sentiment": "STRONG_BULLISH",
            "cmp": 2016.10,
            "one_week_delivery_pct": 54.20,
            "fii_pct": 4.12,
            "dii_pct": 0.35,
            "institutional_trend": "FII continuous buying observed over last 3 sessions",
            "performance": {"stock": 12.40, "sector": 3.10, "index": 0.43},
            "prediction": {"low": 2016.00, "high": 2500.00},
            "quarterlyData": {
                "quarters": ["Q4FY25", "Q1FY26", "Q2FY26", "Q3FY26", "Q4FY26"],
                "revenue": [360.76, 342.10, 315.40, 336.29, 402.52],
                "pat": [40.44, 32.10, 24.50, 30.76, 64.77]
            }
        },
        {
            "company": "Global Geopolitical Headwind",
            "symbol": "CRUDE_MACRO_IMPACT",
            "isin": "GLOBAL_CATALYST",
            "sector": "Aviation & Paint Raw Materials Input",
            "category": "GEOPOLITICAL_WAR_RISK",
            "news_eng": "Macro News: Severe escalation in Middle East geopolitical tensions between Iran and Israel. International Brent crude prices jumped sharply to $95.33 per barrel. This serves as a significant structural negative trigger due to escalating input costs for Indian paint and aviation manufacturing corporations.",
            "news_hin": "ग्लोबल मैक्रो न्यूज: मिडिल ईस्ट में ईरान-इजरायल के बीच भू-राजनीतिक तनाव (Geopolitical Tensions) काफी बढ़ गया है। अंतर्राष्ट्रीय बाजार में ब्रेंट क्रूड ऑयल की कीमत तेजी से बढ़कर $95.33 प्रति बैरल पहुंच चुकी है। क्रूड महंगा होने से भारतीय पेंट और एविएशन कंपनियों के लिए इनपुट कॉस्ट (लागत) बढ़ेगी, जो इनके शेयर की कीमतों के लिए मंदी का ट्रिगर (Negative News) है।",
            "sentiment": "STRONG_BEARISH",
            "cmp": 23483.55,
            "one_week_delivery_pct": 0.0,
            "fii_pct": 0.0,
            "dii_pct": 0.0,
            "institutional_trend": "FII net sellers of ₹3,911 Crores across cash market segment yesterday",
            "performance": {"stock": -0.70, "sector": -1.55, "index": -0.70},
            "prediction": {"low": 23100.00, "high": 23483.55},
            "quarterlyData": None
        }
    ]

def main():
    raw_alerts = fetch_live_nse_regulatory_catalysts()
    
    payload = {
        "lastUpdated": datetime.now().isoformat(),
        "macro": {
            "nifty": "23,483.55 (+0.43%)",
            "sensex": "74,649.84 (+0.52%)"
        },
        "alerts": []
    }
    
    for item in raw_alerts:
        payload["alerts"].append({
            "stockName": item["company"],
            "ticker": item["symbol"],
            "isin": item["isin"],
            "sector": item["sector"],
            "category": item["category"].replace('_', ' '),
            "triggerNewsEnglish": item["news_eng"],
            "triggerNewsHindi": item["news_hin"],
            "sentiment": item["sentiment"],
            "cmp": item["cmp"],
            "deliveryPercentage": item["one_week_delivery_pct"],
            "institutionalHoldings": {
                "fii": item["fii_pct"],
                "dii": item["dii_pct"],
                "trend": item["institutional_trend"]
            },
            "performance": item["performance"],
            "predictionRange": item["prediction"],
            "quarterlyData": item["quarterlyData"]
        })

    with open('premarket_feed.json', 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=4, ensure_ascii=False)
    print("Bilingual technical payload compiled successfully.")

if __name__ == "__main__":
    main()
