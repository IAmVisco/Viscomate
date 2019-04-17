chrome.tabs.query({active: true}, function (tabs) {
    $("#locator").text($("#locator").text() + tabs[0].url);
    console.log(tabs);
});