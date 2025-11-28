# Open Accept Metadata - A Repository for CS Conference Acceptance Rates

> To browse acceptance rates in a more interactive format, please visit the [Open Accept main site](https://openaccept.org/).

Open Accept (OAc) is a collaborative platform for collecting and sharing metadata on paper acceptance rates at global computer science conferences. Our goal is to provide essential insights into the CS research community by aggregating publicly available statistics.

As conference data is often scattered across web platforms and formats, community collaboration is vital to achieving comprehensive, accurate, and up-to-date records. OAc leverages this collaboration to build a centralized, open-source resource for researchers and academia.

## Where can I find the data?
- **Social media platforms**. Researchers frequently share acceptance emails or paper notifications on platforms like Twitter/X, LinkedIn, or Xiaohongshu (Red Note). Search for keywords such as "accepted" or "notification" alongside conference names.
- **Conference websites**. Many venues publish detailed reports directly, such as the [CHI 2025 Paper Outcomes Report](https://chi2025.acm.org/chi-2025-papers-track-post-pc-outcomes-report/).
- **Conference proceddings**. Acceptance rates are often mentioned in the "Preface" or "Chairs' Notes" sections of conference proceedings. For example, see [ICDE 2024 Proceddings, "A Message from the Chairs"](https://ieeexplore.ieee.org/document/10598037).
- **On-site slides**. Chairs may present acceptance statistics during opening or closing sessions. Photos of these slides are sometimes shared on social media.

## How can I contribute?
We welcome community-driven updates to the OAc repository. Follow these steps to contribute:

1. Fork the Repository and make changes.
2. Add a new JSON file (or edit an existing one) that follows the template.
3. Submit a Pull Request with your edits, including clear data sources.
4. The maintainers will review your PR; once approved, it will be merged.

Please note that by contributing, you agree to OAc's [Terms of Use](https://openaccept.org/tou/).

### Data format
All conference entries must be valid JSON and adhere to one of the two templates below.
#### Primary (single‑track) template
```json
{
  "name": "Conference name abbreviation (e.g., AAAI)",
  "full_name": "Conference full name",
  "website": "Website URL",
  "dblp": "DBLP URL",
  "yearly_data": [
    { "year": 2025, "submitted": 12957, "accepted": 3032, "source": "https://url.here" },
    { "year": 2024, "submitted": 9862, "accepted": 2342, "source": "https://url.here" }
  ],
  "sources": [
    "https://urls.here"
  ],
  "remarks": "Any additional notes, optional"
}
```
#### Secondary‑track template
If the conference has a secondary track (currently, OAc only takes *short papers*, *ACL Findings*, and *KDD ADL* into account), please refer to the following template.
```json
{
  "name": "Conference name abbreviation (e.g., AAAI)",
  "full_name": "Conference full name",
  "website": "Website URL",
  "dblp": "DBLP URL",
  "yearly_data": [
    { "year": 2025, "submitted": 12957, "accepted": 3032, "source": "https://url.here" },
    { "year": 2024, "submitted": 9862, "accepted": 2342, "source": "https://url.here" }
  ],
  "second_track": "Findings",
  "second_track_yearly_data": [
    {"year": 2024, "accepted": 976, "submitted": 4407, "source": "https://url.here"},
    {"year": 2023, "accepted": 901, "submitted": 4864, "source": "https://url.here"}
  ],
  "remarks": "Any additional notes, optional",
  "sources": [
    "https://urls.here"
  ]
}
```
| Field | Description | Required | Remarks |
| --- | --- | --- | --- |
| name | Conference abbreviation | Yes | In most cases, the abbr. should be unique, all caps. But there are exceptions, e.g., “RecSys” and “MobiSys”.|
| full_name | Conference full name | Yes ||
| website | Conference website | Yes | If the conference does not have a dedicated website, please use the latest year’s website.|
| dblp | Conference DBLP URL | Yes | |
| yearly_data | Array of yearly data | Yes | Each entry should include the year, # of submitted papers, # of accepted papers, and data source<sup>[1]</sup>. |
| second_track | Secondary track name | Depends<sup>[2]</sup> | If the conference has a secondary track, please specify the track name. |
| second_track_yearly_data | Array of yearly data for the secondary track | Depends<sup>[2]</sup> | Each entry should include the year, # of submitted papers, # of accepted papers, and data source<sup>[1]</sup>. |
|remarks | Additional notes | No | Any additional notes, optional. |
| sources | Array of data sources | No | Where data can be acquired in bulk. For instance, someone's blog that keeps track of acceptance rates over the past few years. |

> [!NOTE]
> - [1]: We strongly suggest including the data source for each entry. If it's a photo taken on-site, please upload to image hosting services such as [Imgur](https://imgur.com/), and [Imgchr](https://imgchr.com/).
> - [2]: Only required when there is a secondary track.


## Add new conferences
OAc primarily adoptes the taxonomy used in [CCF's Recommended International Conferences and Journals Catalog (written in Chinese)](https://www.ccf.org.cn/Academic_Evaluation/By_category/) to categorize conferences into 10 topics:
<ul>
    <li>
        <b>AI</b>:
        Artificial Intelligence</li>
    <li>
        <b>CHI</b>:
        Computer-Human Interaction</li>
    <li>
        <b>DM</b>:
        Database/Data Mining/Information Retrieval
        </li>
    <li>
        <b>GM</b>:
        Computer Graphics/Multimedia</li>
    <li>
        <b>NEW</b>:
        New/Interdiscipline</li>
    <li>
        <b>NET</b>:
        Computer Networks</li>
    <li>
        <b>SEC</b>:
        Networks and Cybersecurity</li>
    <li>
        <b>SW</b>:
        Software Engineering/System Softwares</li>
    <li>
        <b>SYS</b>:
        Computer Systems/Architecture</li>
    <li>
        <b>TH</b>:
        Computing Theory</li>
</ul>

In each category, conferences are classified into four tiers (A, B, C, and TBD) according to CCF's Catalog. [CORE Ranking](https://www.core.edu.au/conference-portal) is also used for reference.

When you propose a conference that is not in either list (CCF's or CORE), please include a brief justification (e.g., “high‑impact venue in the emerging field of...”) in your PR description. Maintainers may need additional discussion time before merging.

## Acknowledgements
Some of the historical data in this repository was gathered from the following sources:
- [Computer Science Conference Statistics](https://csconfstats.xoveexu.com/)
- [Acceptance rates for the <del>major</del> top-tier AI-related conferences](https://github.com/lixin4ever/Conference-Acceptance-Rate)
- [Paper Copilot](https://papercopilot.com/statistics/)

We would like to thank the maintainers of these sources for their endless and valuable efforts to find and share such acceptance rates data.
