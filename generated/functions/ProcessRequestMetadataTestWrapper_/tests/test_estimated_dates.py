
# This file is autogenerated by the gloo compiler
# Do not edit this file directly
# (skip unused imports)
# ruff: noqa: F401
# flake8: noqa
# pylint: skip-file
# isort: skip_file
from .. import ProcessRequestMetadataTestWrapper
from .. import VariantTypes
from ....custom_types import FOIARequestData
from ....custom_types import FoiaTestCasePayload
from ....custom_types import RecordsStatus
from ....custom_types import RequestStatus


import typing
import pytest

InputType = typing.TypeVar('InputType', bound=FoiaTestCasePayload)
OutputType = typing.TypeVar('OutputType', bound=FOIARequestData)

@pytest.mark.gloo_test
@pytest.mark.asyncio
@pytest.mark.parametrize("variant", ['v1'])
class Testestimated_dates:

    async def test_668434(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="668434",
    tid=668434,
    cid=1492848,
    username="Alpha",
    communication="""Dear Ms. Barghouty & Ms. Pickoff-White:

    As you know, this office serves as City Attorneys for the City of Clovis (“City”).  We are in receipt of your Public Records Act (“PRA”) request dated January 23, 2023.  Your request states that it seeks records pursuant to Senate Bills 1421 and 16 for police officer records under the categories identified by Penal Code section 832.7, subdivision (b), for the time period of January 1, 2014, to January 23, 2023.

    On March 17, 2023, the City provided you with “Batch 1” containing responsive, non-exempt documents.  On March 22, 2023, the City provided you with “Batch 2” containing additional responsive, non-exempt documents.  We informed you in our prior correspondence dated April 14, 2023, that the City would make all reasonable efforts to provide further responsive, non-exempt documents to you on a rolling basis in a manner consistent with the PRA by no later than May 19, 2023, provided that we would timely notify you if this was not possible.

    Accordingly, enclosed with the transmission of this correspondence, the City is providing you with further responsive, non-exempt, documents.  This additional set of documents will be referred to as “Batch 3.”  Please note that the City will not disclose information such as personal data, including home addresses or telephone numbers, to preserve the anonymity of family members, whistleblowers, complainants, victims, and witnesses.  (Pen. Code § 832.7, subd. (b)(6).)  Additionally, the City will not release any records which contain sensitive and private information that would constitute an unwarranted invasion of privacy and, therefore, the public interest served by not disclosing the records clearly outweighs the public interest served by disclosure.  (Pen. Code, § 832.7, subd. (b)(7); Gov. Code. § 7922.000.)  Accordingly, such information has been redacted from the documents produced.  Deputy City Attorney Matthew M. Lear is the party responsible for asserting the exemptions.

    Due to the volume of the remaining documents, the City is still in the process of preparing the raw audio/video footage for production.  The City will continue to produce these records on a rolling basis and will make all reasonable efforts to provide the requested records to you in a manner consistent with the PRA.  The City anticipates that it will be able to provide some, if not all, of these remaining documents by no later than June 16, 2023, provided that we will timely notify you if this is not possible.

    We thank you for your continued courtesy.  Please contact me if you have any questions.

    Sincerely,

    LOZANO SMITH



    Matthew M. Lear
    Deputy City Attorney
    City of Clovis

    MML/mc



    Matthew M. Lear | Attorney At Law
    7404 North Spalding Avenue, Fresno, CA 93720-3370
    T: 559.431.5600 F: 559.261.9366
    CONFIDENTIALITY NOTICE: This electronic mail transmission may contain privileged and/or confidential information only for use by the intended recipients. Unless you are the addressee (or authorized to receive messages for the addressee), you may not use, copy, disclose, or distribute this message (or any information contained in or attached to it) to anyone. You may be subject to civil action and/or criminal penalties for violation of this restriction. If you received this transmission in error, please notify the sender by reply e-mail or by telephone at (800) 445-9430 and delete the  transmission.
    """,
    file_text="""""",
    status="partial",
    tracking_number=None,
    date_estimate="2023-06-16",
    price=None
)
        await ProcessRequestMetadataTestWrapper(variant, arg)
        
        

    async def test_670208(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="670208",
    tid=670208,
    cid=1497995,
    username="Alpha",
    communication="""Dear MuckRock Requestor,

    Regrettably, the District will be unable to meet the May 28th, 2023,
    production deadline as previously anticipated. The District expects to
    provide the twelfth installment of records responsive to your November 3,
    2021, request on or before June 15th, 2023. We appreciate your
    understanding and apologize for the delay.

    Ruby Peters
    Public Records Officer
    Mercer Island School District
    206.236.3367


    *Confidentiality Notice:* This email (and any previous email messages or
    attachments thereto) is intended only for use by the addressee(s) named
    herein and may contain legally protected non-public, confidential, and/or
    privileged information intended for the sole use of the designated
    recipient(s). The unlawful interception, use of disclosure of such
    information is strictly prohibited under 18 U.S.C.§ 2511 and any applicable
    law. If you are not an intended recipient of this email, you are hereby
    notified that any dissemination, distribution or copying of this email (and
    any attachments thereto) is strictly prohibited. If you receive this email
    in error please immediately notify me at 206.23.3367
    and permanently delete the
    original email (and any copy of any email) and any printout thereof.""",
    file_text="",
    status="processed",
    tracking_number=None,
    date_estimate="2023-06-15",
    price=None
)
        await ProcessRequestMetadataTestWrapper(variant, arg)
        
        

    async def test_670125(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="670125",
    tid=670125,
    cid=1497915,
    username="Alpha",
    communication="""Good afternoon. I have received your request, and you may expect to hear from me by or before June 7, 2023.

    ----------------------------------------------------------------------------------
    Kathleen Hardy
    CYFD Records Custodian
    PO Drawer 5160
    Santa Fe, NM 87502-5160
    Text : 505-660-8508
    FAX: 505-827-4474
    Report suspected child abuse or neglect by calling #SAFE (#7233) from a cell phone or 1-855-333-SAFE.""",
    file_text="",
    status="processed",
    tracking_number=None,
    date_estimate="2023-06-07",
    price=None
)
        await ProcessRequestMetadataTestWrapper(variant, arg)
        
        

    async def test_670334(self, variant: VariantTypes) -> None:
        arg = FoiaTestCasePayload(
    name="670334",
    tid=670334,
    cid=1498331,
    username="mlrobot",
    communication="""Dear Mr. Delaware,

    Please see the attached letter for an updated estimated completion date for
    your FOIA request 2017-0330-F.

    If I may be of further assistance, please do not hesitate to contact me.

    Sincerely,
    Malisa Culpepper
    FOIA Coordinator""",
    file_text="""May 26, 2023
    Robert Delaware
    DEPT MR 36565
    263 Huntington Ave
    Boston, MA 02115
    Dear Mr. Delaware:
    This correspondence is in response to your email of May 26, 2023 requesting an estimated completion
    date for a FOIA request you have filed with the George W. Bush Presidential Library. That estimate is
    listed below. Our most recent estimate, sent to you on April 26, 2023, was the best estimate we had at that
    time. Currently, we are trying to make our best estimate; however, it is still an estimate. This estimate
    includes time for NARA to complete the necessary notification to the representatives of the former and
    incumbent Presidents in order to afford them an opportunity to conduct a privilege review, as is required
    by the Presidential Records Act (PRA).
    As stated in our letter dated April 27, 2017, request 2017-0330-F is in the complex unclassified electronic
    queue and there are 107 requests ahead of yours in this queue. Per NARA procedures, this request will be
    segmented due to its volume. We will review 10,000 assets and then this request will go to the end of the
    queue. Our best estimate at this time is that the first segment of this request may be completed in
    approximately 20 years from today.
    If you have any questions regarding your FOIA request, please contact our staff at 214-346-1557 or
    gwbush.library@nara.gov. Your FOIA case log number is 2017-0330-F. Please have this number
    accessible for reference during any future contact concerning this case.
    Sincerely,
    Justin Banks
    Supervisory Archivist
    George W. Bush Presidential Library
    JB: MAC""",
    status="processed",
    tracking_number=None,
    date_estimate="2043-05-26",
    price=None
)
        await ProcessRequestMetadataTestWrapper(variant, arg)
        
        