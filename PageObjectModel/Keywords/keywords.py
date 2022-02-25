class LowLevelKeywords:
    def process_keywords(self, keyword, prop_instance, value):
        match keyword:
            case "EnterData":
                prop_instance.send_keys(value)
            case "Click":
                prop_instance.click()
            case "VerifyText":
                assert prop_instance.text == value
            case "ClearText":
                prop_instance.clear()
            case "IsDisplayed":
                assert prop_instance.is_displayed()
            case _:
                raise Exception(f"Keyword {keyword} not supported.")
