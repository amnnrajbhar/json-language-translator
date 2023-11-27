from googletrans import Translator
import json

def translate_json(json_obj, target_language='zh-tw'):
    translator = Translator()

    def translate_value(value):
        translation = translator.translate(value, dest=target_language)
        return translation.text

    def translate_recursive(obj):
        if isinstance(obj, str):
            return translate_value(obj)
        elif isinstance(obj, list):
            return [translate_recursive(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: translate_recursive(value) for key, value in obj.items()}
        else:
            return obj

    translated_json = translate_recursive(json_obj)
    return translated_json

# Example English JSON
english_json = {
    'Dashboard' : 'Dashboard',
  'Colliers_International' : 'Colliers International',
  'Version_Re_connect_17_11_23_4' : 'Version Re_connect_17_11_23_4',
  'Dashboard_Account' : 'Account',
  'Dashboard_Watchlist' : 'Watchlist',
  'Dashboard_Contact' : 'Contact',
  'Dashboard_Activities' : 'Activities',
  'Dashboard_Follow_up' : 'Follow up',
  'Dashboard_Overdue_Follow_Up' : 'Overdue Follow Up',
  'Dashboard_Scan_Business_Card' : 'Scan Business Card',
  'Dashboard_logout_header' : 'Scan Business Card',
  'Dashboard_No' : 'No',
  'Dashboard_Yes' : 'Yes'
}

# Translate JSON to Japanese
japanese_json = translate_json(english_json)

# Print the translated JSON
print(json.dumps(japanese_json, ensure_ascii=False, indent=2))
