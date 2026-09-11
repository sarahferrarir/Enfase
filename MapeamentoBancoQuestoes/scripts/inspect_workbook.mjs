import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const source = process.argv[2];
const input = await FileBlob.load(source);
const workbook = await SpreadsheetFile.importXlsx(input);
const overview = await workbook.inspect({
  kind: "workbook,sheet,table,region",
  maxChars: 20000,
  tableMaxRows: 12,
  tableMaxCols: 30,
  tableMaxCellChars: 160,
});
console.log(overview.ndjson);

for (const sheet of workbook.worksheets.items) {
  const used = sheet.getUsedRange();
  const name = sheet.name;
  console.log(JSON.stringify({ sheet: name, address: used?.address ?? null }));
  if (used) {
    const rows = Math.min(used.rowCount, 15);
    const cols = Math.min(used.columnCount, 40);
    const preview = await workbook.inspect({
      kind: "table",
      sheetId: name,
      range: sheet.getRangeByIndexes(0, 0, rows, cols).address,
      include: "values,formulas",
      tableMaxRows: rows,
      tableMaxCols: cols,
      maxChars: 30000,
    });
    console.log(preview.ndjson);
  }
}

await fs.writeFile("workbook-inspected.ok", "ok\n");
