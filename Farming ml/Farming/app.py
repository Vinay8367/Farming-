import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Complete language translations
TRANSLATIONS = {
    "English": {
        # General
        "title": "Smart Farm Advisor",
        "subtitle": "AI-Powered Agricultural Recommendations",
        "navigation": "Navigation",
        "home": "Home",
        "analytics": "Analytics",
        "weather": "Weather",
        "recommendations": "Recommendations",
        
        # Farm Information
        "farm_info": "Farm Information",
        "current_crop": "Current Crop",
        "farm_area": "Farm Area (acres)",
        "soil_params": "Soil Parameters",
        "soil_ph": "Soil pH",
        "organic_matter": "Organic Matter Content (%)",
        "crop_rotation": "Crop Rotation History",
        "prev_crop": "Previous Crop",
        "seasons_ago": "seasons ago",
        "current_practices": "Current Practices",
        "irrigation_type": "Irrigation Type",
        "fertilizer_category": "Fertilizer Category",
        
        # Crops and Categories
        "crops": {
            "rice": "Rice",
            "wheat": "Wheat",
            "corn": "Corn",
            "soybeans": "Soybeans",
            "cotton": "Cotton"
        },
        "irrigation_types": {
            "drip": "Drip",
            "sprinkler": "Sprinkler",
            "flood": "Flood",
            "rainfed": "Rain-fed"
        },
        "fertilizer_types": {
            "chemical": "Chemical",
            "organic": "Organic",
            "mixed": "Mixed",
            "none": "None"
        },
        
        # Buttons and Actions
        "generate_btn": "Generate Recommendations",
        "analysis_complete": "Analysis complete! See recommendations in the right panel.",
        
        # Quick Stats
        "quick_stats": "Quick Stats",
        "soil_health": "Soil Health Index",
        "water_efficiency": "Water Efficiency",
        "yield_prediction": "Yield Prediction",
        "tons_per_acre": "tons/acre",
        
        # Weather
        "weather_updates": "Weather Updates",
        "current_weather": "Current Weather",
        "precipitation": "Precipitation",
        "wind": "Wind",
        "forecast": "7-Day Forecast",
        "temp_range": "Temperature Range",
        "chance_of_rain": "Chance of Rain",
        
        # Analytics
        "yield_trends": "Yield Trends Over Time",
        "resource_usage": "Resource Usage",
        "resource_efficiency": "Resource Efficiency (%)",
        "cost_analysis": "Cost Analysis",
        "cost_distribution": "Cost Distribution",
        "resources": {
            "water": "Water",
            "fertilizer": "Fertilizer",
            "pesticides": "Pesticides",
            "labor": "Labor"
        },
        "cost_categories": {
            "seeds": "Seeds",
            "fertilizer": "Fertilizer",
            "labor": "Labor",
            "equipment": "Equipment",
            "others": "Others"
        },
        
        # Recommendations
        "crop_management": "Crop Management",
        "resource_optimization": "Resource Optimization",
        "pest_management": "Pest Management",
        "soil_recommendations": """
            Based on your soil pH ({ph}) and organic matter content ({om}%):
            - Apply lime at {lime} tons/acre to optimize soil pH
            - Incorporate cover crops to improve organic matter
            - Consider crop rotation with legumes next season
        """,
        "water_recommendations": """
            Water Management:
            - Implement drip irrigation to improve efficiency
            - Schedule irrigation for early morning
            - Monitor soil moisture using sensors
            
            Fertilizer Plan:
            - Apply NPK in split doses
            - Use organic mulch to retain nutrients
            - Consider foliar application for micronutrients
        """,
        "pest_recommendations": """
            Preventive Measures:
            - Monitor for common pests in your area
            - Maintain field hygiene
            - Use resistant varieties when available
            
            Current Alert:
            - Watch for signs of leaf blast in current weather conditions
        """,
        
        # Footer
        "footer_title": "Smart Farm Advisor | Powered by AI",
        "contact_support": "Need help? Contact support@smartfarm.ai"
    },
    
    "हिंदी": {
        # General
        "title": "स्मार्ट कृषि सलाहकार",
        "subtitle": "एआई-संचालित कृषि सिफारिशें",
        "navigation": "नेविगेशन",
        "home": "होम",
        "analytics": "विश्लेषण",
        "weather": "मौसम",
        "recommendations": "सिफारिशें",
        
        # Farm Information
        "farm_info": "खेत की जानकारी",
        "current_crop": "वर्तमान फसल",
        "farm_area": "खेत का क्षेत्रफल (एकड़)",
        "soil_params": "मिट्टी के मापदंड",
        "soil_ph": "मिट्टी का पीएच",
        "organic_matter": "जैविक पदार्थ सामग्री (%)",
        "crop_rotation": "फसल चक्र इतिहास",
        "prev_crop": "पिछली फसल",
        "seasons_ago": "मौसम पहले",
        "current_practices": "वर्तमान प्रथाएं",
        "irrigation_type": "सिंचाई प्रकार",
        "fertilizer_category": "उर्वरक श्रेणी",
        
        # Crops and Categories
        "crops": {
            "rice": "धान",
            "wheat": "गेहूं",
            "corn": "मक्का",
            "soybeans": "सोयाबीन",
            "cotton": "कपास"
        },
        "irrigation_types": {
            "drip": "टपक सिंचाई",
            "sprinkler": "फव्वारा सिंचाई",
            "flood": "बाढ़ सिंचाई",
            "rainfed": "वर्षा आधारित"
        },
        "fertilizer_types": {
            "chemical": "रासायनिक",
            "organic": "जैविक",
            "mixed": "मिश्रित",
            "none": "कोई नहीं"
        },
        
        # Buttons and Actions
        "generate_btn": "सिफारिशें जनरेट करें",
        "analysis_complete": "विश्लेषण पूर्ण! दाएं पैनल में सिफारिशें देखें।",
        
        # Quick Stats
        "quick_stats": "त्वरित आंकड़े",
        "soil_health": "मिट्टी स्वास्थ्य सूचकांक",
        "water_efficiency": "जल दक्षता",
        "yield_prediction": "उपज पूर्वानुमान",
        "tons_per_acre": "टन प्रति एकड़",
        
        # Weather
        "weather_updates": "मौसम अपडेट",
        "current_weather": "वर्तमान मौसम",
        "precipitation": "वर्षा",
        "wind": "हवा",
        "forecast": "7-दिन का पूर्वानुमान",
        "temp_range": "तापमान सीमा",
        "chance_of_rain": "बारिश की संभावना",
        
        # Analytics
        "yield_trends": "उपज प्रवृत्तियां",
        "resource_usage": "संसाधन उपयोग",
        "resource_efficiency": "संसाधन दक्षता (%)",
        "cost_analysis": "लागत विश्लेषण",
        "cost_distribution": "लागत वितरण",
        "resources": {
            "water": "पानी",
            "fertilizer": "उर्वरक",
            "pesticides": "कीटनाशक",
            "labor": "श्रम"
        },
        "cost_categories": {
            "seeds": "बीज",
            "fertilizer": "उर्वरक",
            "labor": "श्रम",
            "equipment": "उपकरण",
            "others": "अन्य"
        },
        
        # Recommendations
        "crop_management": "फसल प्रबंधन",
        "resource_optimization": "संसाधन अनुकूलन",
        "pest_management": "कीट प्रबंधन",
        "soil_recommendations": """
            आपकी मिट्टी के पीएच ({ph}) और जैविक पदार्थ सामग्री ({om}%) के आधार पर:
            - मिट्टी के पीएच को अनुकूलित करने के लिए {lime} टन/एकड़ चूना लगाएं
            - जैविक पदार्थ बढ़ाने के लिए कवर क्रॉप लगाएं
            - अगले मौसम में दलहनी फसलों के साथ फसल चक्र पर विचार करें
        """,
        "water_recommendations": """
            जल प्रबंधन:
            - दक्षता बढ़ाने के लिए टपक सिंचाई लागू करें
            - सुबह की सिंचाई का समय निर्धारित करें
            - सेंसर का उपयोग करके मिट्टी की नमी की निगरानी करें
            
            उर्वरक योजना:
            - एनपीके को विभाजित खुराक में लागू करें
            - पोषक तत्वों को बनाए रखने के लिए जैविक मल्च का उपयोग करें
            - सूक्ष्म पोषक तत्वों के लिए पर्णीय अनुप्रयोग पर विचार करें
        """,
        "pest_recommendations": """
            निवारक उपाय:
            - आपके क्षेत्र में सामान्य कीटों की निगरानी करें
            - खेत की स्वच्छता बनाए रखें
            - जहां उपलब्ध हो प्रतिरोधी किस्मों का उपयोग करें
            
            वर्तमान चेतावनी:
            - वर्तमान मौसम की स्थिति में लीफ ब्लास्ट के संकेतों पर नज़र रखें
        """,
        
        # Footer
        "footer_title": "स्मार्ट कृषि सलाहकार | एआई द्वारा संचालित",
        "contact_support": "सहायता चाहिए? support@smartfarm.ai पर संपर्क करें"
    },
    
    "తెలుగు": {
        # General
        "title": "స్మార్ట్ వ్యవసాయ సలహాదారు",
        "subtitle": "AI-ఆధారిత వ్యవసాయ సిఫార్సులు",
        "navigation": "నావిగేషన్",
        "home": "హోమ్",
        "analytics": "విశ్లేషణలు",
        "weather": "వాతావరణం",
        "recommendations": "సిఫార్సులు",
        
        # Farm Information
        "farm_info": "పొలం సమాచారం",
        "current_crop": "ప్రస్తుత పంట",
        "farm_area": "పొలం విస్తీర్ణం (ఎకరాలు)",
        "soil_params": "నేల పరామితులు",
        "soil_ph": "నేల pH",
        "organic_matter": "సేంద్రీయ పదార్థ శాతం (%)",
        "crop_rotation": "పంట మార్పిడి చరిత్ర",
        "prev_crop": "గత పంట",
        "seasons_ago": "సీజన్ల క్రితం",
        "current_practices": "ప్రస్తుత పద్ధతులు",
        "irrigation_type": "నీటిపారుదల రకం",
        "fertilizer_category": "ఎరువుల వర్గం",
        
        # Crops and Categories
        "crops": {
            "rice": "వరి",
            "wheat": "గోధుమ",
            "corn": "మొక్కజొన్న",
            "soybeans": "సోయాబీన్స్",
            "cotton": "పత్తి"
        },
        "irrigation_types": {
            "drip": "బిందు సేద్యం",
            "sprinkler": "స్ప్రింక్లర్",
            "flood": "వరద నీటి పారుదల",
            "rainfed": "వర్షాధార"
        },
        "fertilizer_types": {
            "chemical": "రసాయనిక",
            "organic": "సేంద్రీయ",
            "mixed": "మిశ్రమ",
            "none": "ఏదీ కాదు"
        },
        
        # Buttons and Actions
        "generate_btn": "సిఫార్సులను రూపొందించండి",
        "analysis_complete": "విశ్లేషణ పూర్తయింది! కుడి ప్యానెల్‌లో సిఫార్సులను చూడండి.",
        
        # Quick Stats
        "quick_stats": "త్వరిత గణాంకాలు",
        "soil_health": "నేల ఆరోగ్య సూచిక",
        "water_efficiency": "నీటి సామర్థ్యం",
        "yield_prediction": "దిగుబడి అంచనా",
        "tons_per_acre": "టన్నులు/ఎకరం",
        
        # Weather
        "weather_updates": "వాతావరణ నవీకరణలు",
        "current_weather": "ప్రస్తుత వాతావరణం",
        "precipitation": "వర్షపాతం",
        "wind": "గాలి",
        "forecast": "7-రోజుల ముందస్తు అంచనా",
        "temp_range": "ఉష్ణోగ్రత పరిధి",
        "chance_of_rain": "వర్షం సంభావ్యత",
        
        # Analytics
        "yield_trends": "దిగుబడి ధోరణులు",
        "resource_usage": "వనరుల వినియోగం",
        "resource_efficiency": "వనరుల సామర్థ్యం (%)",
        "cost_analysis": "ఖర్చు విశ్లేషణ",
        "cost_distribution": "ఖర్చు పంపిణీ",
        "resources": {
            "water": "నీరు",
            "fertilizer": "ఎరువు",
            "pesticides": "పురుగుమందులు",
            "labor": "కార్మికులు"
        },
        "cost_categories": {
            "seeds": "విత్తనాలు",
            "fertilizer": "ఎరువులు",
            "labor": "కూలీలు",
            "equipment": "పరికరాలు",
            "others": "ఇతరములు"
        },
        
        # Recommendations
        "crop_management": "పంట నిర్వహణ",
        "resource_optimization": "వనరుల అనుకూలీకరణ",
        "pest_management": "పురుగు నిర్వహణ",
        "soil_recommendations": """
            మీ నేల pH ({ph}) మరియు సేంద్రీయ పదార్థ శాతం ({om}%) ఆధారంగా:
            - నేల pH ని అనుకూలపరచడానికి {lime} టన్నులు/ఎకరం సున్నం వేయండి
            - సేంద్రీయ పదార్థాన్ని పెంచడానికి కవర్ క్రాప్స్ వేయండి
            - తదుపరి సీజన్‌లో పప్పుధాన్యాలతో పంట మార్పిడిని పరిగణించండి
        """,
        "water_recommendations": """
            నీటి నిర్వహణ:
            - సామర్థ్యాన్ని మెరుగుపరచడానికి బిందు సేద్యాన్ని అమలు చేయండి
            - ఉదయం సమయంలో నీటి తడిని షెడ్యూల్ చేయండి
            - సెన్సర్లతో నేల తేమను పర్యవేక్షించండి
            
            ఎరువుల ప్రణాళిక:
            - NPK ని విభజించిన మోతాదులలో వేయండి
            - పోషకాలను నిలుపుకోవడానికి సేంద్రీయ మల్చ్ వాడండి
            - సూక్ష్మ పోషకాల కోసం ఆకు ద్వారా వేసే ఎరువులను పరిగణించండి
        """,
        "pest_recommendations": """
            నివారణ చర్యలు:
            - మీ ప్రాంతంలోని సాధారణ పురుగులను పర్యవేక్షించండి
            - పొలం పరిశుభ్రతను నిర్వహించండి
            - అందుబాటులో ఉన్న నిరోధక రకాలను వాడండి
            
            ప్రస్తుత హెచ్చరిక:
            - ప్రస్తుత వాతావరణ పరిస్థితులలో ఆకు మచ్చ వ్యాధి లక్షణాల కోసం గమనించండి
        """,
        
        # Footer
        "footer_title": "స్మార్ట్ వ్యవసాయ సలహాదారు | AI ద్వారా ఆధారితం",
        "contact_support": "సహాయం కావాలా? support@smartfarm.ai ని సంప్రదించండి"
    }
}

# Initialize session state for language
if 'language' not in st.session_state:
    st.session_state.language = "English"

# Page configuration
st.set_page_config(
    page_title="Smart Farm Advisor",
    page_icon="🌾",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stSlider {
        padding: 1rem 0;
    }
    .stSelectbox {
        padding: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Language selector in sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/farm.png")
    selected_language = st.selectbox(
        "Select Language / भाषा चुनें / భాష ఎంచుకోండి",
        ["English", "हिंदी", "తెలుగు"]
    )
    st.session_state.language = selected_language

# Get translations for current language
t = TRANSLATIONS[st.session_state.language]

# Sidebar navigation
with st.sidebar:
    st.title(t["navigation"])
    page = st.radio("Go to", [t["home"], t["analytics"], t["weather"], t["recommendations"]])

# Main content
if page == t["home"]:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title(f"🌾 {t['title']}")
        st.subheader(t["subtitle"])
        
        # Farm Information Form
        st.header(t["farm_info"])
        
        # Basic Info
        col_crop, col_area = st.columns(2)
        with col_crop:
            current_crop = st.selectbox(t["current_crop"], 
                list(t["crops"].values()))
        with col_area:
            farm_area = st.number_input(t["farm_area"], 
                min_value=0.1, value=1.0, step=0.1)

        # Soil Parameters
        st.subheader(t["soil_params"])
        col_ph, col_organic = st.columns(2)
        with col_ph:
            soil_ph = st.slider(t["soil_ph"], 0.0, 14.0, 7.0, 0.1)
        with col_organic:
            organic_matter = st.slider(t["organic_matter"], 
                0.0, 30.0, 2.0, 0.1)

        # Previous Crops
        st.subheader(t["crop_rotation"])
        col_prev1, col_prev2, col_prev3 = st.columns(3)
        with col_prev1:
            prev_crop1 = st.selectbox(f"{t['prev_crop']} (1 {t['seasons_ago']})",
                list(t["crops"].values()))
        with col_prev2:
            prev_crop2 = st.selectbox(f"{t['prev_crop']} (2 {t['seasons_ago']})",
                list(t["crops"].values()))
        with col_prev3:
            prev_crop3 = st.selectbox(f"{t['prev_crop']} (3 {t['seasons_ago']})",
                list(t["crops"].values()))

        # Irrigation and Fertilizer
        st.subheader(t["current_practices"])
        col_irr, col_fert = st.columns(2)
        with col_irr:
            irrigation = st.selectbox(t["irrigation_type"],
                list(t["irrigation_types"].values()))
        with col_fert:
            fertilizer = st.selectbox(t["fertilizer_category"],
                list(t["fertilizer_types"].values()))

        if st.button(t["generate_btn"], type="primary"):
            st.success(t["analysis_complete"])

    # Right Panel
    with col2:
        st.header(t["quick_stats"])
        
        # Stats Cards
        st.metric(t["soil_health"], "76/100", "+5")
        st.metric(t["water_efficiency"], "82%", "-3%")
        st.metric(t["yield_prediction"], f"4.2 {t['tons_per_acre']}", "+8%")
        
        # Weather Updates
        st.header(t["weather_updates"])
        st.markdown(f"🌤️ **{t['current_weather']}:** 24°C, {t['precipitation']}")
        st.markdown(f"🌧️ **{t['precipitation']}:** 30% {t['chance_of_rain']}")
        st.markdown(f"💨 **{t['wind']}:** 12 km/h NE")

elif page == t["analytics"]:
    st.title(t["analytics"])
    
    # Sample data for demonstration
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
    yields = [4.2, 4.1, 4.3, 4.0, 4.4, 4.5, 4.2, 4.3, 4.6, 4.4, 4.2, 4.5]
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Yield': yields
    })
    
    # Plot
    fig = px.line(df, x='Date', y='Yield', 
                  title=t["yield_trends"])
    st.plotly_chart(fig, use_container_width=True)

    # Additional Analytics
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(t["resource_usage"])
        resource_data = {
            'Resource': list(t["resources"].values()),
            'Efficiency': [85, 78, 92, 88]
        }
        resource_df = pd.DataFrame(resource_data)
        fig2 = px.bar(resource_df, x='Resource', y='Efficiency',
                     title=t["resource_efficiency"])
        st.plotly_chart(fig2)

    with col2:
        st.subheader(t["cost_analysis"])
        cost_data = {
            'Category': list(t["cost_categories"].values()),
            'Cost': [2000, 3500, 4000, 1500, 1000]
        }
        cost_df = pd.DataFrame(cost_data)
        fig3 = px.pie(cost_df, values='Cost', names='Category',
                     title=t["cost_distribution"])
        st.plotly_chart(fig3)

elif page == t["weather"]:
    st.title(t["weather"])
    
    # 7-day forecast
    st.subheader(t["forecast"])
    forecast_data = {
        'Day': ['Today', 'Tomorrow', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],
        'Temp_High': [24, 25, 23, 26, 24, 22, 25],
        'Temp_Low': [18, 19, 17, 20, 18, 16, 19],
        'Precipitation': [10, 30, 0, 0, 20, 60, 10]
    }
    
    df_forecast = pd.DataFrame(forecast_data)
    
    # Display forecast
    for idx, row in df_forecast.iterrows():
        col1, col2, col3 = st.columns([1,2,1])
        with col1:
            st.write(f"**{row['Day']}**")
        with col2:
            st.write(f"🌡️ {row['Temp_Low']}°C - {row['Temp_High']}°C")
        with col3:
            st.write(f"☔ {row['Precipitation']}%")
        st.divider()

elif page == t["recommendations"]:
    st.title(t["recommendations"])
    
    # Generate recommendations based on input
    st.header(t["crop_management"])
    st.info(t["soil_recommendations"].format(ph=7.0, om=2.0, lime=2))
    
    st.header(t["resource_optimization"])
    st.success(t["water_recommendations"])
    
    st.header(t["pest_management"])
    st.warning(t["pest_recommendations"])

# Footer
st.markdown("---")
st.markdown(f"### 🌾 {t['footer_title']}")
st.markdown(t["contact_support"])