function doGet(req) {
  var doc = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = doc.getSheetByName('sheet1');
  var values = sheet.getDataRange().getValues();

  var output = [];
  for(var i = 1; i<values.length; i++){
    var row = {};
    row['name'] = values[i][2];
    row['called'] = values[i][4];
    row['money'] = values[i][5];
    output.push(row);
  }
  return ContentService.createTextOutput(JSON.stringify({trip: output, count: output.length, with_gender: false})).setMimeType(ContentService.MimeType.JSON);
}