# Agent Guide for `python-copier-template-example`

This file is for AI coding agents working in this repository. It states how
to run the checks and where edits belong. The human-facing contribution
guide is [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Commands

The `task` task runner drives the common commands:

```sh
task fix            # auto-fix formatting and lint
task lint           # ruff format --check + ruff check (check-only)
task test           # pytest
task type-check     # type checker + static analysis
task check          # everything above
```

Run `task fix` before committing to apply formatting
and lint fixes, then `task check` (or `lint` + `test`
+ `type-check` individually) before finishing a change.
The repo-hygiene checks (secrets, workflow linting, YAML validity,
conventional commit messages) run in CI, not as local hooks — the lint and
fix tasks work anywhere, including outside a git repository.

Type checking uses basedpyright plus `pyrefly`; `deptry`,
`vulture`, and `typos` also run as part of type-check.


Build the docs with `task docs`.

## Where to edit

- Application/package code: `src/python_copier_template_example/`
- Tests: `tests/`
- Docs: `README.md` and `docs/`

Keep 100% coverage where it exists; do not lower it.


Data, notebooks, and reports (`data/`, `notebooks/`, `models/`,
`reports/`) are analysis artifacts — keep generated outputs out of git.

## Commits and CI

- Use [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, ...); the repository's hygiene CI enforces it on commit
  messages and the PR title.
- CI runs lint, type-check, and tests on every push
 plus a docs build; keep all of them green.

## Field rules (ethics appendix)

Field rules the generator matched to this project kind (crypto choices,
dependency license drift, data-collection copyright, LLM/MCP tool
security, model-evaluation fairness), plus the rules your `domain_traits`
answer selected (biometric identification, medical device software). Each
section opens with a scope blockquote: if its triggers do not apply to the
code you are editing, skip that section. Sections are written in Japanese.

# ライセンス変動 — 依存の現行ライセンスを追跡し、BSL/SSPL混入を防ぐ

> **適用条件**: 依存パッケージ・ツールチェーン・コンテナイメージを
> 追加・更新する場面すべて。フォーク元が非OSS化した事例の引用も含む。
> 規模: 世界問題(ライセンス変更はどの法域でも起き、汚染は世界の
> リポジトリに広がる)。
> 配布: library / cli / script / web / data-science(依存を1つでも
> 持つ全プロジェクト種別)。
> 要約: (1)追加時に現行ライセンスを確認し、allowlistと照合する
> (2)BSL/SSPL等のソース可用ライセンスを確認なしで混入させない
> (3)フォーク移行(Terraform→OpenTofu等)は正当な後継を通す。
> 詳細は本文。
> Triggers: `(?i)\b(licen[cs]e|bsl|busl|sspl|rsal|elv2|copyleft|gpl|agpl|lgpl|terraform|opentofu|elasticsearch|redis|source-available)\b`.

## 事実

HashiCorpは2023-08-10、TerraformをMPL 2.0からBusiness Source License
(BUSL 1.1)へ変更した。コミュニティはフォークOpenTofuを設立し、
Linux Foundation傘下で継続している。2024-04にHashiCorpはOpenTofuに対し
BSL適用後コードの不正利用を主張する書簡を送付し、OpenTofuは公開で反論した
(MPL 2.0版のコードに基づくとする立場。係争は公開記録の範囲で確認できる)。
方向が逆の例もある: Elasticは2024-08にElasticsearchへAGPLv3を
追加選択肢として復帰させ、Redisも2025-05にAGPLv3を追加した。
つまり依存のライセンスは「追加時点の記憶」では正しくなく、
リポジトリ単位で変動する。BUSL自体は発行からChange Date(原則4年)経過で
指定ライセンスへ切り替わるため、版ごとに扱いが変わる点にも注意する。
出典: HashiCorp公式ブログ、OpenTofu FAQ(REGISTRY.ymlに記録)。

## 禁止パターン

- ライセンス確認なしの依存追加(BSL/SSPL/RSAL/ELv2等のソース可用、
  強copyleftの確認漏れ)。
- フォーク元・フォーク先の取り違え(Terraform本家をMPL 2.0と誤記載、
  OpenTofuをBUSLと誤記載)。
- 「昔追加したからOSSのはず」という版の据え置き(renovateやlock更新で
  ライセンス欄を再確認しない運用)。
- ライセンス表示の捏造(README/NOTICEに実態と異なる表記)。

## 推奨設定

- allowlist方針を明文化(Apache-2.0/MIT/BSD/MPL-2.0等を許可、
  GPL系は配布形態照合、BSL/SSPLは例外承認制)。
- 依存ライセンスの列挙と照合は、生成物に同梱の `license-check` タスクが
  行う(`pip-licenses --from=mixed --partial-match`。security推奨で有効、
  CIのlintジョブから呼ばれる。fail-on はプロジェクトのライセンスから
  自動導出: permissive/Proprietary等→GPL系(LGPL/AGPL含む)、
  GPL/LGPL→AGPL、AGPL→なし=最強なので打ち止め)。質問票が提示する
  全ライセンスがポリシーに解決される(取りこぼすと「絶対に落ちない
  license-check」が同梱され、本節の L2 主張が嘘になる)。`--partial-match` は
  部分一致なので、`GPL` は `GNU General Public License (GPLv3)` /
  `...(LGPL)` / `...(AGPLv3)` のいずれにも当たる。タスクを落とした
  構成では同型の照合(`pip-licenses`相当でlicense欄を出力しallowlistと照合)を
  自前で組む。
- renovate等の自動更新でメジャー更新・ライセンス欄変化を通知対象にする。
- 競合サービスを作る予定がある場合、SSPL/BSL類は「自分が提供する形」で
  制限に触れるため、早期に弁護士照会(本節はその判断の代行ではない)。

## 運用チェック

- 設定側トリガー(Copier QA L1用):
  `(?i)\b(BUSL|SSPL|RSAL|ELv2|licen[cs]e)\b`
  hit時は本節の存在をassert。
- 依存のライセンス棚卸しを半期に一度、pyproject/lockの差分レビューで
  実施する。担当: 依存管理と同じレビュー役。

## 制度変更ウォッチ

- 変更予告: HashiCorpとOpenTofuの係争は動き得る。確度: 係争中(公開記録)。
  Elastic/Redisの復帰のように逆方向の変更もあり得る。
- 確認TODO: OpenTofu FAQとHashiCorp公式の現行方針を一次で確認
  (review_by: 2027-03-31)。
- 影響TODO: 自プロジェクトがTerraform/OpenTofu類のツールを参照する場合、
  どちらを後継として扱うかドキュメントに明記する。

<!-- 法的助言ではない。専門家レビュー必須。 / This is not legal advice; expert review required. -->

# AIと著作権 — 取得・学習・RAGコードは「非享受目的」を壊さない

> **適用条件**: ウェブ取得(スクレイピング)、データセット構築、
> fine-tuning、RAG/検索、生成物の再配布を実装する場面。
> 日本法(著作権法30条の4)を軸に、法域差の注意も併記する。
> 規模: 国内問題(30条の4は日本法で、権利者の利益も国内法がまず守る)。
> 配布: cli / data-science(取得・学習・RAGコードを書くもの)。
> 要約: (1)robots.txt等の取得拒否措置を回避しない (2)表現そのものを
> 検索・再出力するRAG設計をしない(事実・概念の要約抽出にとどめる)
> (3)模倣を目的とする過学習・特定作品群の追加学習をしない。
> 詳細は本文。
> Triggers: `(?i)\b(scrap|crawl|robots\.txt|rag|retrieval|fine-?tun|dataset|embedding|public[- ]domain|copyright)\b`.

## 事実

文化庁は2024-03、著作権審議会の議論を経て「AIと著作権に関する
考え方について」を公表した。情報解析を目的とする著作物の利用は
著作権法30条の4で原則適法だが、「著作権者の利益を不当に害する場合」は
権利制限の対象外とされる。同考え方は、(1)特定の表現を忠実に再現させる
目的の過学習や特定作品群のみの追加学習は「表現の享受」目的と評価され
30条の4が適用されない、(2)RAGでデータベース内の創作的表現そのものを
検索・取得して出力に含める設計は享受目的の併存が問題になり得る、
(3)robots.txt等の取得拒否措置の意図的な回避は、将来的な有償の
データ解析市場を不当に害し得る、と整理した。生成物の侵害判断は
従来法理と同じく「類似性」と「依拠性」で行われ、学習データ内に
元作品があり生成結果に創作的特徴が感得できれば依拠性が推認され得る。
また保護期間は法域差(死後70年原則、戦時加算、映画・企業名義の扱い)が
あり、パブリックドメイン判定は対象法域ごとの照合が要る。
出典: 文化庁「AIと著作権に関する考え方について」(REGISTRY.ymlに記録)。

## 禁止パターン

- 取得拒否措置の回避(`ROBOTSTXT_OBEY=False`、UA偽装、
  レート制限回避のためのIPローテーション等)。
- 特定作家・特定リポジトリの文体/実装を再現させるfine-tuning・
  ワンショット模倣プロンプト。
- RAGで原文の表現(コードの連続行、文章段落)をそのまま検索・出力する設計
  (要約・埋め込み化でなく生チャンクを返す構成)。
- 出典を記録せずに取得データを学習/RAG基盤へ流す。
- 「パブリックドメイン」の無検証前提(法域・保護期間の照合なし利用)。

## 推奨設定

- 保持は事実・概念レベルに(要約、埋め込み、統計)。生表現の保持は
  ライセンス/利用規約の確認を通したものに限定し、出典を版管理する。
- 出力側に重複検出を入れる(既知ソースとの長い共通n-gramで
  差し戻すフィルタ)。
- 取り込み工程に利用規約・ライセンス確認ステップを置き、
  拒否措置(robots.txt/ToS)の有無をデータセットのメタデータに記録する。
- パブリックドメイン判定は法域+著作者の没年/公表年を入力にする
  チェッカーを通し、判定根拠を残す。

## 運用チェック

- 設定側トリガー(Copier QA L1用):
  `(?i)\b(robots|scrapy|BeautifulSoup|httpx|rag|chromadb|faiss|langchain)\b`
  hit時は本節の存在をassert。
- 取得コードのレビュー項目に「拒否措置の尊重/レート/UAの正直さ」を置く。
  担当: データ取得を実装するレビュー役。

## 制度変更ウォッチ

- 変更予告: 文化庁はAIと著作権の論点の継続的な整理を続けており、
  追加の考え方・論点整理が出る可能性。確度: 審議中。
- 確認TODO: 文化庁ページで最新の考え方・Q&Aを一次で確認
  (review_by: 2027-03-31)。
- 影響TODO: 自プロジェクトの学習/RAGデータの取得元一覧に対し、
  拒否措置の現状を再確認する。

<!-- 法的助言ではない。専門家レビュー必須。 / This is not legal advice; expert review required. -->

# MLバイアス — 集団別評価・説明可能性・人間確認を評価に組み込む

> **適用条件**: モデル学習・評価パイプライン、スクリーニング/判定
> ロジック、データセット構築で、人に関する予測を扱う場面。
> 規模: 世界問題(偏ったデータはどの国の集団にも不利に働き得る)。
> 配布: data-science / kaggle(モデル学習・評価を含むもの)。
> 要約: (1)平均精度だけでなく集団別の性能を必ず出す (2)protected
> attributeのdropだけで差別を消したことにはしない(proxy対策)
> (3)生命機会に影響する判断は人間確認を必須にする。詳細は本文。
> Triggers: `(?i)\b(fairness|bias|demographic|subgroup|shap|xai|explainab|protected|disparate|equalized|parity)\b`.

## 事実

学習データの集団偏りは実害として報告されている。経皮的動脈血酸素飽和度
計(パルスオキシメータ)では、黒人患者で「実は低酸素なのに計測値が
正常を示す」見えない低酸素血症の頻度が約3倍になるという分析が
2020年に報告され、デバイス・データ収集の偏りが臨床判断の歪みに
直結する例とされた。EU AI Act(2024-08-01発効)は高リスクAIの
学習/検証/テストデータにバイアス観点での検査と、関係する代表性を
要求し(第10条)、展開者への基本的権利影響評価(FRIA)も定める。
fairness指標は相互に両立しないことが数学的に示されているため、
「どの指標を選んだか、何を捨てたか」の文書化が実務上の最低要件になる。
出典: Sjoding et al. (NEJM 2020)、EU AI Act(REGISTRY.ymlに記録)。

## 禁止パターン

- protected attribute(人種・性別・年齢等)の列dropだけで対処完了と
  する設計(proxy変数(郵便番号、病院ID等)が実質復元する)。
- 平均精度だけの報告(集団別sensitivity/specificity/FPRを出さない)。
- 生命機会(医療、雇用、融資、法執行)での自動確定(人間確認なしの
  単独判断)。
- fairness指標の無文書選択(指標変更がレビューなしで行われる)。
- 評価データの学習データへの混入(集団別評価を不能にする)。

## 推奨設定

- 評価レポートの既定形に集団別表を含める(サブグループ ×
  sensitivity/specificity/FPR。サンプル小集団は区間表示で出す)。
- 指標選択の文書化(demographic parity と equalized odds は通常両立
  しない。選んだ指標と捨てた指標をREADME/モデルカードに明記)。
- 説明可能性: SHAP等のfeature attributionをレビュー工程に置き、
  proxy由来の重み変数を点検する。
- データセットにdatasheet(収集方法・人口構成・既知の偏り)を添付する。
- 分布ドリフトの監視と再評価トリガーを設け、性能の維持を前提にしない。
- 最終判断は人間(専門家)が行うUI/フローを既定にする。

## 運用チェック

- 設定側トリガー(Copier QA L1用):
  `(?i)\b(fairlearn|shap|groupby\(.*(race|gender|age|sex)|fairness|subgroup)\b`
  hit時は本節の存在をassert。
- モデルリリースのチェックリストに「集団別表の添付」「指標選択の
  文書」を置く。担当: 実験レビュー役。

## 制度変更ウォッチ

- 変更予告: EU AI Actの高リスク義務は段階適用(2026-08-02一般適用、
  他の規制対象製品に組み込まれる高リスクは2027-08-02)。
  確度: 施行済(スケジュール確定)。
- 確認TODO: 第10条・FRIAの実務ガイダンス(委員会ガイドライン)の公表を確認
  (review_by: 2026-12-18)。
- 影響TODO: 自プロジェクトの評価レポートテンプレートに集団別表を
  組み込む。

<!-- 法的助言ではない。専門家レビュー必須。 / This is not legal advice; expert review required. -->
