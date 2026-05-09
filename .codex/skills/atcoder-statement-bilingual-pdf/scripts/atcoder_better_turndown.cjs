const fs = require("fs");
const { JSDOM } = require("jsdom");
const TurndownService = require("turndown");

function readStdin() {
  return fs.readFileSync(0, "utf8");
}

function normalizeCodeWithBreaks(html) {
  return html
    .replace(/\r\n/g, "\n")
    .replace(/\r/g, "\n")
    .replace(/<br\s*\/?>/gi, "<br>")
    .replace(/\n+/g, "\n")
    .trim();
}

function normalizeTableCellMarkdown(markdown) {
  return markdown
    .replace(/\r\n/g, "\n")
    .replace(/\r/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .replace(/\n/g, "<br>")
    .replace(/\|/g, "\\|")
    .trim();
}

function normalizeMathText(text) {
  return (text || "")
    .replace(/\u00a0/g, " ")
    .replace(/\r\n/g, "\n")
    .replace(/\r/g, "\n")
    .trim();
}

function createTurndownService(document) {
  const turndownService = new TurndownService({ bulletListMarker: "-" });

  turndownService.keep(["del"]);

  turndownService.addRule("removeByClass", {
    filter(node) {
      if (!node.classList) {
        return node.nodeName === "SCRIPT" || node.nodeName === "STYLE";
      }
      return (
        node.classList.contains("html2md-panel") ||
        node.classList.contains("div-btn-copy") ||
        node.classList.contains("btn-copy") ||
        node.classList.contains("ojb-overlay") ||
        node.classList.contains("monaco-editor") ||
        node.nodeName === "SCRIPT" ||
        node.nodeName === "STYLE"
      );
    },
    replacement() {
      return "";
    },
  });

  turndownService.addRule("atcoder-var", {
    filter(node) {
      return node.nodeName === "VAR";
    },
    replacement(content, node) {
      const latex = normalizeMathText(node.textContent);
      return latex ? `$${latex}$` : "";
    },
  });

  turndownService.addRule("inline-math", {
    filter(node) {
      return node.tagName && node.tagName.toLowerCase() === "span" && node.className === "katex";
    },
    replacement(content, node) {
      const latex = normalizeMathText(node.querySelector("annotation")?.textContent);
      return latex ? `$${latex}$` : "";
    },
  });

  turndownService.addRule("block-math", {
    filter(node) {
      return node.tagName && node.tagName.toLowerCase() === "span" && node.className === "katex-display";
    },
    replacement(content, node) {
      const latex = normalizeMathText(node.querySelector("annotation")?.textContent);
      if (!latex) {
        return "";
      }
      return `\n$$\n${latex}\n$$\n`;
    },
  });

  turndownService.addRule("pre", {
    filter(node) {
      return node.tagName && node.tagName.toLowerCase() === "pre";
    },
    replacement(content, node) {
      if (node.classList.contains("source-code-for-copy") || node.classList.contains("prettyprint")) {
        return "";
      }
      const body = content.replace(/\n+$/, "");
      return `\n\`\`\`text\n${body}\n\`\`\`\n`;
    },
  });

  turndownService.addRule("details", {
    filter(node) {
      return node.tagName && node.tagName.toLowerCase() === "details";
    },
    replacement(content, node) {
      const summary = node.querySelector("summary")?.textContent?.trim() || "";
      const cloned = node.cloneNode(true);
      const clonedSummary = cloned.querySelector("summary");
      if (clonedSummary) {
        clonedSummary.remove();
      }
      const body = turndownService.turndown(cloned.innerHTML).trim();
      const parts = [];
      if (summary) {
        parts.push(`**${summary}**`);
      }
      if (body) {
        parts.push(body);
      }
      return `\n\n${parts.join("\n\n")}\n\n`;
    },
  });

  turndownService.addRule("bordertable", {
    filter: "table",
    replacement(content, node) {
      if (!node.classList.contains("table")) {
        return content;
      }
      const rows = Array.from(node.querySelectorAll("tr"));
      if (rows.length === 0) {
        return "";
      }

      function renderCell(cell) {
        const singleCode = cell.children.length === 1 && cell.firstElementChild?.tagName?.toLowerCase() === "code";
        if (singleCode && cell.querySelector("br")) {
          const codeHtml = normalizeCodeWithBreaks(cell.firstElementChild.innerHTML);
          return `<code>${codeHtml}</code>`;
        }
        return normalizeTableCellMarkdown(turndownService.turndown(cell.innerHTML.trim()));
      }

      const headerCells = Array.from(rows[0].querySelectorAll("th, td"));
      const header = `| ${headerCells.map(renderCell).join(" | ")} |`;
      const separator = `| ${headerCells.map(() => " --- ").join("|")} |`;
      const body = rows.slice(1).map((row) => {
        const cells = Array.from(row.querySelectorAll("td, th"));
        return `| ${cells.map(renderCell).join(" | ")} |`;
      });

      return `\n\n${[header, separator, ...body].join("\n")}\n\n`;
    },
  });

  const anchors = document.querySelectorAll("a[href]");
  anchors.forEach((anchor) => {
    const href = anchor.getAttribute("href");
    if (!href) {
      return;
    }
    try {
      const absolute = new URL(href, "https://atcoder.jp").toString();
      anchor.setAttribute("href", absolute);
    } catch (error) {
      // Ignore invalid URLs and keep the original value.
    }
  });

  return turndownService;
}

function main() {
  const raw = readStdin();
  const payload = JSON.parse(raw || "{}");
  const html = payload.html || "";
  const dom = new JSDOM(`<body>${html}</body>`);
  const { document } = dom.window;
  const turndownService = createTurndownService(document);
  const markdown = turndownService
    .turndown(document.body.innerHTML)
    .replace(/\r\n/g, "\n")
    .replace(/\r/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
  process.stdout.write(markdown);
}

main();
