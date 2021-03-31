var = {
    "id": "b1e9727a-d522-45e8-8311-b6b01054af25",
    "version": "2.0",
    "name": "Test_broker_acc",
    "url": "https://prerelease.smarttrader.com",
    "tests": [{
        "id": "d16b8392-987f-44f2-9ed1-0f7a8b7db513",
        "name": "Test_broker_acc",
        "commands": [{
            "id": "2b64a52b-c1e6-4c2a-99e0-051379ea822e",
            "comment": "",
            "command": "open",
            "target": "/",
            "targets": [],
            "value": ""
        }, {
            "id": "d7aff018-cea4-44a3-bee9-28c4eec99d43",
            "comment": "",
            "command": "setWindowSize",
            "target": "1936x1056",
            "targets": [],
            "value": ""
        }, {
            "id": "211020c5-7e9f-445c-b5cd-029b2f81628f",
            "comment": "",
            "command": "click",
            "target": "css=.landing-header__navigation > .landing-header__nav-link:nth-child(1)",
            "targets": [
                ["css=.landing-header__navigation > .landing-header__nav-link:nth-child(1)", "css:finder"],
                ["xpath=//a[contains(text(),'Charts')]", "xpath:link"],
                ["xpath=//div[@id='LandingPageContainer']/div/div/div/div/div[2]/nav/a", "xpath:idRelative"],
                ["xpath=//a[contains(@href, '/charts/')]", "xpath:href"],
                ["xpath=//nav/a", "xpath:position"]
            ],
            "value": ""
        }, {
            "id": "2d417f3e-58d5-4b04-9db8-ff2315603bbb",
            "comment": "",
            "command": "runScript",
            "target": "window.scrollTo(0,0)",
            "targets": [],
            "value": ""
        }, {
            "id": "3209ee2d-eaa3-41d6-b387-90558fae0fc3",
            "comment": "",
            "command": "runScript",
            "target": "window.scrollTo(0,0)",
            "targets": [],
            "value": ""
        }, {
            "id": "8109ace1-b545-401d-ac4a-3118fc6b07e4",
            "comment": "",
            "command": "click",
            "target": "css=.ucpicon-trading-b",
            "targets": [
                ["css=.ucpicon-trading-b", "css:finder"],
                ["xpath=//div[@id='dashboard']/div/div[3]/div[3]/div[3]/div/i", "xpath:idRelative"],
                ["xpath=//div[3]/div[3]/div[3]/div/i", "xpath:position"]
            ],
            "value": ""
        }, {
            "id": "c7740b2c-f6e6-4316-85f3-22e4605c240a",
            "comment": "",
            "command": "click",
            "target": "linkText=Manage Accounts",
            "targets": [
                ["linkText=Manage Accounts", "linkText"],
                ["css=.dropdown-list .tradingSignIn", "css:finder"],
                ["xpath=//a[contains(text(),'Manage Accounts')]", "xpath:link"],
                ["xpath=//div[@id='dashboard']/div/div[3]/div[3]/div[3]/div[2]/div/ul/li/a", "xpath:idRelative"],
                ["xpath=//div[2]/div/ul/li/a", "xpath:position"],
                ["xpath=//a[contains(.,'Manage Accounts')]", "xpath:innerText"]
            ],
            "value": ""
        }, {
            "id": "12b528f5-fa60-47b4-ab9a-edc9b5ee8155",
            "comment": "",
            "command": "click",
            "target": "id=addAccountBtn",
            "targets": [
                ["id=addAccountBtn", "id"],
                ["css=#addAccountBtn", "css:finder"],
                ["xpath=//button[@id='addAccountBtn']", "xpath:attributes"],
                ["xpath=//div[@id='manageAccountsDialog']/div/div/div[3]/button[2]", "xpath:idRelative"],
                ["xpath=//div[3]/button[2]", "xpath:position"]
            ],
            "value": ""
        }]
    }],
    "suites": [{
        "id": "84619398-780f-44af-bc7a-0482fedb4baa",
        "name": "Default Suite",
        "persistSession": False,
        "parallel": False,
        "timeout": 300,
        "tests": ["d16b8392-987f-44f2-9ed1-0f7a8b7db513"]
    }],
    "urls": ["https://prerelease.smarttrader.com/"],
    "plugins": []
}
