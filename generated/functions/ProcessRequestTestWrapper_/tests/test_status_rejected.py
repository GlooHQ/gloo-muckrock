
# This file is autogenerated by the gloo compiler
# Do not edit this file directly
# (skip unused imports)
# ruff: noqa: F401
# flake8: noqa
# pylint: skip-file
# isort: skip_file
from .. import ProcessRequestTestWrapper
from .. import VariantTypes
from ....custom_types import FOIARequestData
from ....custom_types import FoiaTestCasePayload
from ....custom_types import RecordsStatus
from ....custom_types import RequestStatus


import typing
import pytest

pytest_plugins = ["gloo_py.testing.pytest_gloo"]

InputType = typing.TypeVar('InputType', bound=FoiaTestCasePayload)
OutputType = typing.TypeVar('OutputType', bound=FOIARequestData)

@pytest.mark.gloo_test
@pytest.mark.asyncio
@pytest.mark.parametrize("variant", ['v1'])
class Teststatus_rejected:

    async def test_667892(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="667892",
    tid=667892,
    cid=1492026,
    username="Alpha",
    communication="""We are in receipt of your public records request maintained by the Hamilton County Sheriff\'s office https://www.hcso.org/public-records-requests/ and the Hamilton County Clerk of Courts office https://www.courtclerk.org/records-search/request-records/                        You made the request to the Hamilton County Board of County Commissioners. RC 149.43 provides for access to public records kept in the custody of a \"public body.\" Unfortunately, the Board of County Commissioners does not have custody of any records that would be responsive to your request and must deny your request at this time.

If you have any questions or concerns regarding this request, please feel free to contact me.

Lisa Daria
Hamilton County Administration
The Todd B. Portune Center for County Government
138 East Court Street, Room 603
Cincinnati, OH  45202
513-946-4438""",
    file_text="""Hamilton County
Administration

Daria, Lisa MAY 18 a0
From: Doherty, Bridget
Sent: Thursday, May 18,2023 10:53 AM
Tor Daria, Lisa
Subject: FW: Ohio Open Records Law Request: Andrew Ross Mitchell Records Request
Can you take this one?

Bridget oherty

Communications Manager,

Hamiton County Adminiraton

emai ridges doher@hamitoncoorg

Phone: 513.946.403 | Mobi: 513.656.0149

Todd . Fortune Cente for County Goverment
EBIOED 5c am cos, ciocnon on 5208
From: 145883-84493254@requests muckrock com <145883-84493254@requests.muckrock.com>
Sent: Thursday, May 18, 2023 10:46 AM
To: Doherty, Bridget <Bridget. Doherty @hamilton-co.org>
Subject: Ohio Open Records Law Request: Andrew Ross Mitchell Records Request
Hamilton County (OH)
Ohio Open Records Law Office
Rm 603
138 East Court Street
Cincinnati, OH 45202
May 18,2023
To Whom It May Concern:
Pursuant to the Ohio Open Records Law, hereby request the following records:
Any arrest records for Andrew Ross Mitchell (DOB: 01/26/1982), redacted version is okay. |
Any arrest reports for Andrew Ross Mitchell (DOB: 01/26/1982), redacted version i okay.
Any Mugshots for Andrew Ross Mitchell (DOB: 01/26/1982)
Any jail housing records for Andrew Ross Mitchell (DOB: 01/26/1982). |
Any current or prior restraining orders sued upon Andrew Ross Mitchell (DOB: 01/26/1982).
The requested documents will be made available tothe general public, and this request is not being made for
commercial purposes. |
In the event that there are fees, | would be grateful f you would inform me of the total charges in advance of fufiling |
my request. | would prefer the request filed electronically, by e-mail attachment if available or CD-ROM if not.
! |


Thankonin Aare ore ste pas i sta ek fr ecg on sponse os |
request within 10 business days.
Sincerely,
Charlotte Mitchell
View request history, upload responsive documents, and report problems here:
hitps://accounts.muckrock,com/accounts/login/2next=https%3A%2F%2Fwww.muckrock.com3Ã©2Faccounts2Flogin%2E
343Fne%3D%252Faccounts3252Fagency login%252Fhailton-county-oh-4524%252Fandrew-ross-mitchell-records-
request-145883%252F%253Femail%253DBridget, Doherty3252540hamilton:
co.0rgurl auth token=AAB3fcoN34 hP111x-0sZM Jzew33ALpzesvik3AWQOVIILVAIfIEZHYC2KEAM3USVa-IDF514955-
8f3C0
If prompted for a passcode, please enter:
GRMBVMIG
Filed via MuckRock com
E-mail (Preferred): 145883-84493254 @requests.muckrock com
PLEASE NOTE OUR NEW ADDRESS
For mailed responses, please address (see note):
MuckRock News
DEPT MR 145883
263 Huntington Ave
Boston, MA 02115
PLEASE NOTE: This request is not filed by a MuckRock staff member, but is being sent through MuckRock by the above in
order to better track, share, and manage publi records requests. Also note that improperly addressed (i.., with the
requester\'s name rather than \"MuckRock News\" and the department number) requests might be returned as.
undeliverable.

2""",
    status="rejected",
    tracking_number="None",
    date_estimate="None",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        

    async def test_667580(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="667580",
    tid=667580,
    cid=1491616,
    username="Alpha",
    communication="""DOI-OS-2017-000115 has been processed with the following final disposition: Other.""",
    file_text="""None""",
    status="rejected",
    tracking_number="OS-2017-00527",
    date_estimate="None",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        

    async def test_668946(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="668946",
    tid=668946,
    cid=1495533,
    username="Alpha",
    communication="""Good afternoon,

A response to FOIA # 05863038 was sent to 142098-03362166@requests.muckrock.com<mailto:142098-03362166@requests.muckrock.com> on April 5th, 2023 at 2:33PM CST. Please see that e-mail for the FOIA response.

Respectfully,

Illinois State Police
FOIA Office""",
    file_text="""None""",
    status="rejected",
    tracking_number="05863038",
    date_estimate="2023-03-28",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        

    async def test_669304(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="669304",
    tid=669304,
    cid=1496654,
    username="Alpha",
    communication="""Hello -

Attached is the Final Agency Decision regarding your FOIA or Privacy Act Appeal with the Office of General Counsel, Information & Administrative Law Group.


Please note, this email box it not monitored. If you are filing a new FOIA or Privacy Act Appeal, you can email it to: OGCFOIAAppeals@va.gov<mailto:OGCFOIAAppeals@va.gov>

Thank you,

U.S. Department of Veteran Affairs
Office of General Counsel (024)
Information & Administrative Law Group
FOIA & Privacy Act Appeals
[Logo  Description automatically generated]""",
    file_text="""U.S. Department of Veterans Affairs
Office of General Counsel
Information and Administrative Law Group
810 Vermont Avenue NW
Washington DC 20420
www.va.gov/ogc

 In Reply Refer To: 024L
OGC Case #: 158825
FOIA Request #: 22-02290-F
May 23, 2023
MuckRock News
Attn: Mr. Ryan Thompson
DEPT MR 122329
411A Highland Avenue
Somerville, MA 02144-25
122329-06534997@requests.muckrock.com
Dear Mr. Thompson:
This is the final agency decision issued under the Freedom of Information Act
(FOIA), 5 U.S.C. Â§ 552, in response to your appeal from the initial agency decision
issued by the Department of Veterans Affairs (VA) Office of General Counsel (OGC).
For the reasons outlined below, your appeal is denied.
Procedural History
Initial request On January 3, 2022, you submitted a FOIA request for the
following information:
Copies of any and all Settlement Agreement(s) of the
Valentini v. Shinseki Federal Court Case(s) and its related
Action(s), that were entered into by and between the
Plaintiff(s) and Defendant(s) in that Case; wherever such
Agreement(s) to any of the aforementioned Case(s) and
Action(s) exist, if any.
You provided background regarding your request, including that âValentini v. Shinseki
is a Civil Rights Case filed in the Federal Court for the Central District of California in
2011 under Case Number 2:11-cv-04846â and that VA is one of the Defendants in the
case. You claimed that there is no settlement agreement entered or â[n]oticed to the
Valentini Court and / or Entered upon itâs Docket(s)â despite a âFinal Judgment Order of
February 17th, 2015 in That Case expressly Orders âShould this matter fail to resolve
itself, the Court shall reinstate all previously issued order.ââ

Fees VAâs FOIA regulations require each request to be characterized under 38
C.F.R. Â§ 1.561(c) and fees to be estimated and charged, when applicable. Your request
was characterized as a âNews Mediaâ requester. You were not charged any fees for the
processing of this request.
Search On January 6, 2022, OGC FOIA Officer Gregory Draves requested
responsive records from the Real Property Law Group (RPLG), which is the practice
group within OGC that worked on the Valentini litigation. The RPLG attorney assigned
to the litigation searched Outlook for the terms âValentini settlementâ and âValentini v.
Shinseki.â The search produced a copy of the 2015 settlement agreement and a
restatement of the settlement agreement executed by the parties in 2017. The attorney
also noted that the 2015 agreement is publicly available at the following address:
https://www.westladraftmasterplan.org/documentation/extra-info.
Initial Agency Decision (IAD) On January 11, 2021, Mr. Draves issued an IAD,
notifying you that responsive records had been located. He identified two (2)
documents, totaling seven (7) pages, as responsive to your request. He provided the
two documents to you in their entirety. You were also provided with the appropriate
appeal, mediation, and public liaison rights.
Responsive Records The documents disclosed to you consisted of (1)
Restatement of Settlement Agreement (dated January 12, 2017) â four (4) pages; and
(2) Principles for a Partnership and Framework for Settlement By and Between the U.S.
Department of Veterans Affairs (dated January 28, 2015) â three (3) pages.
Appeal In a letter dated March 8, 2022, and received in our office on March 23,
2022, you appealed the full grant IAD. You argued that the document dated January 28,
2015, is not a settlement agreement because it âdoes not state nor stipulate anywhere
therein, that it is the very Settlement Agreement to any Federal Action whatsoeverâ and
it is âexpressly not enforceable in any court, about various expectations, between
persons who were not Plaintiffs in Valentini v. Shinsekiâ¦â
You also questioned the responsiveness of the document dated January 12,
2017. You wrote that it refers to an agreement signed on January 28, 2015, and you
claim that âno such referred-to agreement exists, unless it has never been Released to
the Publicâ¦â You also write that even if it did exist, it is not a settlement agreement in
Valentini v. Shinseki because the plaintiffs in Valentini v. Shineski âare not a private nonï¿¾profit corporation named Vets Advocacy.â You also claim that neither of the two
signatories to the document, Ronald Olson and Ann Brown, are party to the Valentini v.
Shineski litigation.
You also claim that the two documents âdo not appear to be registered and
accepted by the Valentini Court on the Federal Docket of that Action. In fact, the Case
Record Notices, well after January 15, 2015 â that the actual parties to Valentini v.
Shinseki purportedly intended to stipulate to settle in the future.â You also stated that âit

appears the Plaintiffs in the Action were never present in session after they Prevailed,
as in Won the Case, in Fall of 2013.â
Relevant Law We have thoroughly reviewed your appeal under the provisions of the
FOIA, which provides that federal agencies must disclose records requested unless
they may be withheld in accordance with one or more of nine statutory exemptions. 5
U.S.C. Â§ 552(b).
Analysis You appear to question the adequacy of the records search and whether the
documents provided to you are, in fact, the documents you requested. Mr. Draves
contacted an OGC attorney with first-hand knowledge of the Valentini litigation, who
searched for and located the two (2) settlement agreements. We believe the efforts
taken to locate the documents you seek were sufficient to satisfy the duty of the
Department under the FOIA to conduct a reasonable search.
Furthermore, we have examined both documents and the docket history for Case
No. 2:11-cv-04846 in the U.S. District Court for the Central District of California. Based
on our careful review, we conclude that the two (2) documents are responsive to, and
fulfill, your request. We address each of your arguments, below, in turn.
You identify three (3) alleged issues with the January 28, 2015 (âJanuary 2015â)
document. You state that it is not a settlement agreement because âit does not state or
stipulate anywhere therein, that it is the very Settlement Agreement to any Federal
Action whatsoeverâ¦â Please note that the preamble of the document states that it is
between the VA and representatives of the plaintiffs in the Valentini case. Paragraph 5
of the document also states that the parties will file a joint motion in the District Court
âfor an indicative ruling that, in light of the partiesâ commitment to work as partners, the
District court would vacate its judgment in Valentini v. McDonald . . . and coordinate to
file additional pleadings . . . as well as pleadings necessary to effect a dismissal without
prejudice of the entire actionâ¦â That the January 2015 document does not contain your
preferred specific wording does not mean it is not a settlement agreement. You also
take issue with the fact that Paragraph 14 of the document states that it is ânot intended
to be enforceable in any courtâ¦â We note that lack of enforceability in court does not
negate the fact that the January 2015 document is a settlement agreement, which
ultimately resulted in the case being dismissed. Finally, you argue that the January 2015
document is âbetween persons who were not Plaintiffsâ in the litigation. Please note that
attorney Ronald Olson signed the agreement âon behalf of all plaintiffsâ and, as such, it
was not necessary for each individual plaintiff to sign.
We further direct your attention to the docket for Case No. 2:11-cv-04846 in the
U.S. District Court for the Central District of California. As discussed in the January
2015 document, Electronic Court Filing (ECF) 188 is a Notice of Motion and Joint Motion
for Order for Indicative Ruling Pursuant to Fed. R. Civ. P. 62.1. The document states:
âThe Plaintiffs and Government Defendants (the âmoving partiesâ) have recently reached
agreement to work together in partnership to address these important challenges rather

than continue this litigation.â ECF 196 is a Joint Stipulation to Dismiss Case, which
states: âThe parties further stipulate that this dismissal shall be without prejudice, and
that each party shall bear its own costs. The reasons for this dismissal have been set
forth previously in the Joint Motion To Vacate Judgment Pursuant to Fed. R. Civ. P.
60(b), ECF 193, as well as in the Joint Motion for Indicative Ruling Pursuant to Fed. R.
Civ. P. 62.1, ECF 188, and have been addressed in the Courtâs orders granting the
above-referenced motions. See Order, February 17, 2015, ECF 194; Order, February
3, 2015, ECF 189.â If you have further questions regarding the January 2015 settlement
agreement and the conclusion of the litigation, we suggest you review the
aforementioned court filings.
You also identified three (3) alleged issues with the January 12, 2017 (âJanuary
2017â) document. You wrote that the January 2017 document references an agreement
signed on January 28, 2015, that does not exist, unless it has never been publicly
released. The referenced January 28, 2015, document is the previously discussed
January 2015 settlement agreement that was disclosed to you. You also suggest that
the January 2017 document is not a settlement in the Valentini case because the
plaintiffs in Valentini âare not a private non-profit corporation named Vets Advocacy.â
Per the January 2015 settlement, the Plaintiffsâ representatives formed a non-profit
corporation âto help meet the objective and goalsâ of the January 2015 settlement. That
non-profit is Vets Advocacy. You also claim that neither of the two (2) signatories to the
document, Mr. Ronald Olson and Ms. Ann Brown, are party to the Valentini litigation.
Mr. Olson, who signed the January 2015 agreement on behalf of all plaintiffs, signed
the January 2017 agreement as a representative of Vets Advocacy, where he serves
on the Board of Directors. Ms. Brown signed the agreement in her capacity as the VA
Medical Center Director, on behalf of the VA, who was a party to the litigation.
We would also like to direct your attention to publicly available information
regarding the settlement and the Valentini litigation. As the RPLG attorney noted,
settlement information is available on the VA Greater Los Angeles Healthcare System
Draft Master Plan website. See https://www.westladraftmasterplan.org/. On the âAboutâ
page, the timeline includes a link to the Valentini v. McDonald settlement in the â1st
Quarter 2015.â See https://www.westladraftmasterplan.org/about. The site describes
the settlement as follows: âOn January 28, 2015, former VA Secretary Robert McDonald
settled a class action lawsuit against the Department of Veterans Affairs alleging VA
was mismanaging the West LA Campus, by allowing commercial uses of land versus
using the land to support and care for our nationâs Veterans. VA and representatives of
the plaintiffs pledged to work together as partners to end veteran homelessness in the
Greater Los Angeles area.â On the âLibraryâ page, under âSource & Update Documentsâ
and then âBackground Information,â there are links to both âSettlement Agreement â
2015â and âRestatement of Settlement Agreement â 2017â for download. See
https://www.westladraftmasterplan.org/documentation/extra-info. They are the same
documents that were disclosed to you.

Additionally, the Vets Advocacy website states that it is a ânon-profit organization
facilitating revitalization of the U.S. Department of Veterans Affairs West Los Angeles
campus as a condition of the Valentini v. Shinseki settlement.â See
https://www.vatherightway.org/vets-advocacy/. On that same website, when you click
on âSettlement Agreementâ on the timeline for January 2015, the following description
appears: âVA Secretary Bob McDonald and Plaintiff Partners sign the âPrinciples for
Partnership and Framework for Settlementâ agreement which called for the creation of
a veterans homelessness strategy, mutual cooperation in the development of a Master
Plan to set out the most effective use of the campus for veterans, development of an
exit strategy for leases not pertaining to veteran healthcare or housing and the creation
of a non-profit entity (Vets Advocacy) to assist in such efforts. Both parties also agreed
to file a joint motion to the District Court that would vacate its judgment in Valentini v.
McDonald.â A link to the January 28, 2015, document is also available.
Conclusion Based upon the foregoing, your appeal is denied.
Mediation and Appeal Rights This final agency decision concludes the
administrative processing of your appeal.
As part of the 2007 FOIA amendments, the Office of Government Information
Services (OGIS) was created to offer mediation services. Similarly, as part of the FOIA
Improvement Act of 2016, VA established a FOIA Public Liaison to offer mediation
services. Both OGIS and the VA Public Liaison will assist in resolving disputes between
FOIA requesters and VA as a non-exclusive alternative to litigation. Using OGIS or the
VA FOIA Public Liaison does not affect your right to pursue litigation. You may contact
OGIS or the VA Public Liaison in any of the following ways:
Office of Government Information Services E-mail: ogis@nara.gov
National Archives and Records Administration Telephone: 202-741-5770
Room 2510 Facsimile: 202-741-5769
8601 Adelphi Road Toll-free: 1-877-684-6448
College Park, MD 20740-6001
VA FOIA Public Liaison E-mail: vacofoiaservice@va.gov
James Killens III Telephone: 1-877-750-3642
VA FOIA Service Facsimile: 202-632-7581
810 Vermont Avenue, NW (005R1C)
Washington, DC 20420

With respect to any information denied to you by this final agency decision, the
FOIA requires us to advise you that if you believe the Department erred in this decision,
you have the right to file a complaint in an appropriate United States District Court.
 Sincerely,

 Deputy Chief Counsel
 Office of General Counsel,
 Information and Administrative Law
 Group (IALG)
CC: Gregory Draves, FOIA Officer, OGC
Michael Sarich, VA FOIA Service Director
VACO FOIA Service""",
    status="rejected",
    tracking_number="22-02290-F",
    date_estimate="None",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        

    async def test_667950(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="667950",
    tid=667950,
    cid=1492088,
    username="Alpha",
    communication="""Mr. Feathers:

You missed the deadline to appeal our response sent on December 14, 2022.
We now consider the matter closed.

Respectfully,

*Ron Smith*
Controller & Records Officer
*Weber State University*
*3850 Dixon Parkway, Dept 1014*
*Ogden, UT  84408-1014*
*801 626-6613*""",
    file_text="""None""",
    status="rejected",
    tracking_number="None",
    date_estimate="None",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        

    async def test_667568(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="667568",
    tid=667568,
    cid=1491604,
    username="Alpha",
    communication="""DOI-OS-2017-000207 has been processed with the following final disposition: Other.""",
    file_text="""None""",
    status="rejected",
    tracking_number="OS-2017-00759",
    date_estimate="None",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        

    async def test_669869(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="669869",
    tid=669869,
    cid=1497078,
    username="Alpha",
    communication="""This is an automated message from the DC Government FOIA system. Dear Emma Best, The status for your request is below. Please log into https://foia-dc.gov/palMain.aspx and go to Request Status. If you have any questions regarding the status of your request, please contact the agency\'s FOIA office that you had submitted your FOIA request to. You can communicate directly with the FOIA office by clicking on Inbox, search the request number, and then click Compose Message. OR, visit to see a list DC Government FOIA Office’s/officer’s contact information and have your Request ID ready. (https://dc.gov/node/818962) Contact FOIA Office Request status: Closed Request ID: 2020-FOIA-06542 Description: To Whom It May Concern:Pursuant to the DC Freedom of Information Act, I hereby request the following records:1. Documents mentioning, describing or generated in response to the BlueLeaks release, the preceding hack or subsequent fallout, including but not limited to:* Damage assessments* Emails* Interagency communications (local, state, or federal)* Communications with the press about BlueLeaks* Communications with Twitter or other social media or sharing platforms2. Documents mentioning or describing Distributed Denial of Secrets (DDoSecrets)You may limit this request to records generated between November 1, 2018 and the present.I am a member of the news media and request classification as such. I have previously written about the government and its activities, with some reaching over 100,000 readers in outlets such as Gizmodo, MuckRock, Motherboard, Property of the People, Unicorn Riot, and The Outline, among others. As such, as I have a reasonable expectation of publication and my editorial and writing skills are well established. In addition, I discuss and comment on the files online and make them available through non-profits such as the library Internet Archive and the journalist non-profit MuckRock, disseminating them to a large audience. While my research is not limited to this, a great deal of it, including this, focuses on the activities and attitudes of the government itself. As such, it is not necessary for me to demonstrate the relevance of this particular subject in advance.As my primary purpose is to inform about government activities by reporting on it and making the raw data available, I request that fees be waived.The requested documents will be made available to the general public, and this request is not being made for commercial purposes.In the event that there are fees, I would be grateful if you would inform me of the total charges in advance of fulfilling my request. I would prefer the request filled electronically, by e-mail attachment if available or CD-ROM if not.Thank you in advance for your anticipated cooperation in this matter. I look forward to receiving your response to this request within 15 business days, as the statute requires.Sincerely,Emma BestUpload documents directly: https://https://www.muckrock.comhttps://accounts.muckrock.com/accounts/login/?next=https%3A%2F%2Fwww.muckrock.com%2Faccounts%2Flogin%2F%3Fnext%3D%252Faccounts%252Fagency_login%252Fmetropolitan-police-department-385%252Fblueleaks-metropolitan-police-department-96897%252F%253Femail%253DFOIA.SystemAdmin%252540dc.gov&url_auth_token=AAAVLaR50UI9LAIrJLVbEMzyFG8%3A1jv6cL%3AuxCY87eJhiW3faMYKyl39g2td4o Regards,
DC Government FOIA Portal""",
    file_text="""None""",
    status="rejected",
    tracking_number="2020-FOIA-06542",
    date_estimate="None",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        

    async def test_669180(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="669180",
    tid=669180,
    cid=1496489,
    username="Alpha",
    communication="""Consistent with the language included in *all* FOIA responses from our
office, to the extent you consider any part of a response a denial, the
responsibility of the West Virginia Department of Homeland Security to
respond to your initial request is at an end.
If you feel information contained in the response is contrary to law, you
may institute an action for declaratory and/or injunctive relief in the
Circuit Court of the county in which you assert the records are kept,
subject to all jurisdictional procedural prerequisites, which are
specifically not waived.
Further, if you seek additional information, please send a new FOIA
request, as the responsibility of the West Virginia Department of Homeland
Security to respond to your initial request is at an end.

--

Brandolyn N. Felton-Ernest, Esq.

Deputy General Counsel

Department of Homeland Security

Office of the Cabinet Secretary

1900 Kanawha Blvd., East

Building 1, Suite 400-W

Charleston, WV  25305

Office Phone – (304) 558-2930

Direct Dial - (304) 205-6834

Mobile Phone – (304) 553-2698

Fax - (304) 558-6221



*CONFIDENTIAL: ATTORNEY - CLIENT PRIVILEGED COMMUNICATION*

* ***************************************************************************



The information contained in this electronic message is legally privileged
and confidential under applicable law and is intended for the use of the
individual/s or entity named above.  If the recipient of this message is
not the above-named recipient, you are hereby notified that any
dissemination, copy or  disclosure of this communication is strictly
prohibited.  If you have received this communication in error,  please
notify the sender at 304.558.2930.""",
    file_text="""None""",
    status="rejected",
    tracking_number="None",
    date_estimate="None",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        

    async def test_669182(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="669182",
    tid=669182,
    cid=1496491,
    username="Alpha",
    communication="""--- Please respond above this line ---


Thank you for your updated request, Regarding your request for records involving Daniel Espinoza Flores: District Attorney\'s Office investigation of the incident found no significant injuries or trauma caused by the use of force . Moreover , it was determined that the use of force was not the cause of death. Therefore, the records sought are not subject to disclosure pursuant to Penal Code section 832 7(b)
Police reports, investigations and recordings are generally exempt from disclosure through the Public Records Request system under Government Code 7923.600.
If you believe there is a valid exemption, please let me know.
Sgt. McCaskill
mmccaskill@fullertonpd.org
714-738-5336
To monitor the progress or update this request please log into the Fullerton Public Records Center (https://u8387778.ct.sendgrid.net/ls/click?upn=6HtRfOYLt5fXvpttM-2FU1HVfFXt3IhMDjzgmztLHrVQFWo4PAXpZQEd-2FHNJDoaUtVoGYX4FKLQzR5NxqtYrySncUdSmv7SRpS7rkkpdUkvWs-3DMfzU_P2CsNFfhZzmd360sZf2N1ukIfJpDpGVkp3fbym2QZgY94q-2Bggjpv4s0tzXvEwX7WrygvnLaWkRet9yYjdWfAWen56IukJeYGxTmqDRT4HwouEqR74vgLFFeoMzXgAWhkowLVC7ZDJylYNHv0vynXpQZ8LvYWeA-2FHtd-2FjL0TgJNf6a2QJNGBnhJY08uBnpq8YTe4pkr3T5Fv0-2B9Nni04e7-2B8QPvhEdvo4RJm2Zxl7MAA-3D)""",
    file_text="""None""",
    status="rejected",
    tracking_number="R000061-012323",
    date_estimate="None",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        

    async def test_669870(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="669870",
    tid=669870,
    cid=1497079,
    username="Alpha",
    communication="""This is an automated message from the DC Government FOIA system. Dear Emma Best, The status for your request is below. Please log into https://foia-dc.gov/palMain.aspx and go to Request Status. If you have any questions regarding the status of your request, please contact the agency\'s FOIA office that you had submitted your FOIA request to. You can communicate directly with the FOIA office by clicking on Inbox, search the request number, and then click Compose Message. OR, visit to see a list DC Government FOIA Office’s/officer’s contact information and have your Request ID ready. (https://dc.gov/node/818962) Contact FOIA Office Request status: Closed Request ID: 2020-FOIA-00182 Description: To Whom It May Concern:Pursuant to the Freedom of Information Act, I hereby request the following records:Records describing, authorizing or mentioning expenses or personnel assignments in response to or accommodation of visits from officials in the federal government between January 1, 2001 and the present.I am a member of the news media and request classification as such. I have previously written about the government and its activities, with some reaching over 100,000 readers in outlets such as Gizmodo, MuckRock, Motherboard, Property of the People, Unicorn Riot, and The Outline, among others. As such, as I have a reasonable expectation of publication and my editorial and writing skills are well established. In addition, I discuss and comment on the files online and make them available through non-profits such as the library Internet Archive and the journalist non-profit MuckRock, disseminating them to a large audience. While my research is not limited to this, a great deal of it, including this, focuses on the activities and attitudes of the government itself. As such, it is not necessary for me to demonstrate the relevance of this particular subject in advance.As my primary purpose is to inform about government activities by reporting on it and making the raw data available, I request that fees be waived.The requested documents will be made available to the general public, and this request is not being made for commercial purposes.In the event that there are fees, I would be grateful if you would inform me of the total charges in advance of fulfilling my request. I would prefer the request filled electronically, by e-mail attachment if available or CD-ROM if not.Thank you in advance for your anticipated cooperation in this matter. I look forward to receiving your response to this request within 20 business days, as the statute requires.Sincerely,Emma BestUpload documents directly: https://https://www.muckrock.comhttps://accounts.muckrock.com/accounts/login/?url_auth_token=AAAVLaR50UI9LAIrJLVbEMzyFG8%3A1iHVhS%3AFKzqQWraX87SUWL87WrASapU-BI&next=https%3A%2F%2Fwww.muckrock.com%2Faccounts%2Flogin%2F%3Fnext%3D%252Faccounts%252Fagency_login%252Fmetropolitan-police-department-385%252Fexpenditures-relating-to-visits-from-federal-officials-metropolitan-police-department-80492%252F%253Femail%253DFOIA.SystemAdmin%252540dc.gov Regards,
DC Government FOIA Portal""",
    file_text="""None""",
    status="rejected",
    tracking_number="2020-FOIA-00182",
    date_estimate="None",
    price=None
)
        await ProcessRequestTestWrapper(variant, arg)
        
        
