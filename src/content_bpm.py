# -*- coding: utf-8 -*-
"""HDSD BPM · phiếu có bước trình ký E-Sign (kiểu mới: Liên kết Yêu cầu ký + khối Kết quả ký)."""
BP = 'https://bpm.base.com.vn'
SV = BP + '/service/aFCazn7Q-A9livnQOYj-ixztmnOHi64'
BUILD = SV + '/build'
SET = BP + '/settings/services'
ES = 'https://esign.base.com.vn'

PAGE = dict(
    app='bpm', client='Traphaco',
    title=('HDSD BPM · Phiếu có trình ký · Traphaco', ''),
    h1=('Hướng dẫn BPM · Trình ký trong quy trình', 'BPM guide · Signing inside a flow'),
    eyebrow=('HƯỚNG DẪN SỬ DỤNG · BPM', 'USER GUIDE · BPM'),
    hero_h=('Phiếu đi tới bước ký, <em>KÝ XONG TỰ CHẠY TIẾP</em>', 'The job reaches signing and <em>MOVES ON ONCE SIGNED</em>'),
    hero_lead=('6 bước, 4 vai trò: <b>người lập phiếu</b> tạo công việc và bấm Trình ký, <b>người ký</b> ký ngay trong BPM, khối <b>Kết quả ký</b> chờ chữ ký rồi rẽ nhánh Đã ký / Từ chối, <b>quản trị</b> dựng Liên kết Yêu cầu ký và luồng.',
               '6 steps, 4 roles: <b>requesters</b> create the job and click Trình ký, <b>signers</b> sign inside BPM, the <b>Kết quả ký</b> block waits and branches Signed / Declined, <b>admins</b> build the signing link and flow.'),
    hero_img='bpm_cv_chokyketqua', hero_float=('Traphaco · bpm.base.com.vn · 14/11/2026', 'Traphaco · bpm.base.com.vn · 14 Nov 2026'),
    kpi=[('6', ('bước hướng dẫn', 'guided steps')), ('4', ('vai trò', 'roles')), ('{{nimg}}', ('ảnh thật đánh số', 'numbered screenshots')), ('{{niss}}', ('tình huống xử lý', 'fixes'))],
    band1=('Mục 1–3 · Phiếu chạy thế nào, ký ở đâu', 'Sections 1–3 · How the job flows, where signing happens'),
    band2=('Mục 4–5 · 6 bước, ảnh thật có đánh số', 'Sections 4–5 · 6 steps, numbered real screenshots'),
    band3=('Mục 6 · Gõ vấn đề, ra cách xử lý', 'Section 6 · Type a problem, get the fix'),
    band4=('S1–S9 · Dịch vụ, trường tệp, Liên kết Yêu cầu ký, khối Kết quả ký', 'S1–S9 · Service, file field, signing link, signing-result block'),
    t_flow=('1 · Lưu đồ phiếu có trình ký', '1 · Job flow with signing'),
    l_flow=('Hàng = ai làm; cột = bước. Bấm một ô để tới hướng dẫn.', 'Rows = who; columns = steps. Click a box to jump.'),
    flowcards=[(('Mũi tên xanh đậm', 'Navy arrows'), ('Phiếu chuyển giữa người: lập → trình ký → ký.', 'The job moving between people: create → submit → sign.')),
               (('Mũi tên xanh lá', 'Green arrows'), ('BPM / E-Sign tự làm: tạo hồ sơ ký, chờ kết quả, rẽ nhánh, ghi kết quả về phiếu.', 'BPM / E-Sign: create envelope, wait, branch, write back.')),
               (('Nét đỏ', 'Red lines'), ('Từ chối ký: mặc định kết thúc phiếu (Thất bại), hoặc nối về bước có người để Trình lại.', 'Declined: ends the job (Failed) by default, or loops to a human step to resubmit.'))],
    t_status=('2 · Trạng thái công việc và yêu cầu ký', '2 · Job and signing-request statuses'), l_status=None,
    t_ben=('3 · Lợi ích đo được', '3 · Measurable benefits'),
    l_ben=('<b>Chắc chắn</b> = đọc từ hệ thống. <b>Mục tiêu</b> = đề xuất, cần chốt mốc gốc với Traphaco.', '<b>Certain</b> = read from the system. <b>Target</b> = proposed, baseline to agree with Traphaco.'),
    t_matrix=('4 · Hành trình × Vai trò', '4 · Journey × Roles'),
    t_ai=('5 · Dùng AI trong BPM', '5 · Using AI in BPM'), l_ai=None,
    t_iss=('6 · Tra cứu tình huống phát sinh', '6 · Find a fix'),
    t_setup=('7 · Quản trị cần setup gì', '7 · What admins must set up'),
    l_setup=('Làm theo thứ tự S1 → S9 trên dịch vụ TEST “Đề nghị thanh toán có trình ký”. Dịch vụ thật “1. QT thanh toán - ký số” chỉ xem, không sửa.', 'Follow S1 → S9 on the TEST service. The real service was only viewed.'),
    checklist=('Checklist khi thêm bước trình ký vào quy trình', 'Checklist when adding signing to a flow'),
    footer=('Base.vn × Traphaco · Ảnh chụp hệ thống thật trên tenant demo, dữ liệu TEST · 14/11/2026', 'Base.vn × Traphaco · Real screenshots on the demo tenant, TEST data · 14 Nov 2026'),
    issph=('Gõ vấn đề, vd: không có nút Trình ký, đã ký mà phiếu không chạy, từ chối…', 'Type a problem, e.g. no Trình ký button, signed but stuck, declined…'),
)

ROLES = [
    dict(id='LP', color='#1352d0', name=('Người lập phiếu / Kế toán', 'Requester / Accountant'), short=('Người lập', 'Requester'), desc=('Tạo công việc, đính kèm tờ trình, bấm Trình ký.', 'Creates the job, attaches the memo, clicks Trình ký.')),
    dict(id='NK', color='#16a34a', name=('Người ký (Giám đốc)', 'Signer (Director)'), short=('Người ký', 'Signer'), desc=('Ký ngay trong BPM hoặc từ email E-Sign.', 'Signs inside BPM or from the E-Sign email.')),
    dict(id='TD', color='#ffb300', name=('Người theo dõi / Chủ bước', 'Follower / Step owner'), short=('Theo dõi', 'Follower'), desc=('Xem tiến độ, xử lý khi kẹt.', 'Watches progress, unblocks.')),
    dict(id='QT', color='#8b5cf6', name=('Quản trị BPM', 'BPM admin'), short=('Quản trị', 'Admin'), desc=('Dựng trường, Liên kết Yêu cầu ký, khối Kết quả ký.', 'Builds fields, signing link, result block.')),
]
SHORT = {'B1': ('Làm quen', 'Get started'), 'B2': ('Tạo phiếu', 'Create'), 'B3': ('Trình ký', 'Send to sign'), 'B4': ('Chuyển chờ ký', 'Wait'), 'B5': ('Ký', 'Sign'), 'B6': ('Kết quả', 'Result')}
RMAP = {
    'B1': {'LP': 'm', 'NK': 'm', 'TD': 'm', 'QT': 'p'},
    'B2': {'LP': 'm'},
    'B3': {'LP': 'm', 'QT': 'p'},
    'B4': {'LP': 'm', 'TD': 'p'},
    'B5': {'NK': 'm', 'LP': 'p'},
    'B6': {'LP': 'm', 'TD': 'm', 'QT': 'p'},
}
RDO = {
    'B1': {'LP': ('Xem luồng của dịch vụ.', 'Read the service flow.'), 'NK': ('Biết chỗ ký: thẻ Cần bạn ký.', 'Know where to sign.'), 'TD': ('Theo dõi Pipeline.', 'Watch the Pipeline.'), 'QT': ('Hỗ trợ người dùng.', 'Support users.')},
    'B2': {'LP': ('Tạo công việc, tải tờ trình PDF.', 'Create the job, upload the memo PDF.')},
    'B3': {'LP': ('Bấm + Trình ký, đặt ô ký, Gửi ký.', 'Click + Trình ký, place field, send.'), 'QT': ('Liên kết phải bật ở bước.', 'The link must be on for the step.')},
    'B4': {'LP': ('Submit bước để phiếu sang Kết quả ký.', 'Submit so the job waits at the result block.'), 'TD': ('Thấy phiếu ở cột Chờ ký.', 'See it in the waiting column.')},
    'B5': {'NK': ('Bấm Ký ngay, áp chữ ký.', 'Click Ký ngay, apply signature.'), 'LP': ('Theo dõi tab Liên kết.', 'Watch the Liên kết tab.')},
    'B6': {'LP': ('Kiểm tra phiếu đã hoàn thành.', 'Check the job completed.'), 'TD': ('Xử lý nhánh Từ chối.', 'Handle declines.'), 'QT': ('Chỉnh nhánh nếu cần Trình lại.', 'Adjust the decline branch.')},
}
STATUS = dict(
    main=[('Start', 'Start', '#94a3b8'), ('Kế toán trình ký', 'Accountant submits', '#1352d0'), ('Kết quả ký · Chờ ký', 'Signing result · Waiting', '#ffb300'), ('End · Đã hoàn thành', 'End · Completed', '#16a34a')],
    side=[('Từ chối / Hết hạn → Thất bại', 'Declined / Expired → Failed', '#ff3b5c')],
    note=('Yêu cầu ký có trạng thái riêng: Đang chờ bạn → Đã hoàn thành (1/1). Kết quả ký chốt danh sách khi vào bước rồi chờ đủ chữ ký.', 'Signing requests have their own status. The result block locks the list on entry and waits for all signatures.'),
)
FLOW = dict(
    lanes=[('LP', 'Người lập / Kế toán', 'Requester', '#1352d0'), ('NK', 'Người ký', 'Signer', '#16a34a'), ('SYS', 'BPM · E-Sign tự động', 'BPM · E-Sign auto', '#94a3b8')],
    nodes=[
        ('a1', 0, 'LP', ('Xem luồng', 'Pipeline / Quy trình'), ('Read flow', 'Pipeline / Flow')),
        ('b1', 1, 'LP', ('Tạo công việc', '+ tờ trình PDF'), ('Create job', '+ memo PDF')),
        ('c1', 2, 'LP', ('+ Trình ký', 'đặt ô ký · Gửi'), ('+ Trình ký', 'field · Send')),
        ('c2', 2, 'SYS', ('Tạo hồ sơ', 'E-Sign'), ('Envelope', 'E-Sign'), 'n sys'),
        ('d1', 3, 'LP', ('Submit bước', ''), ('Submit step', '')),
        ('d2', 3, 'SYS', ('Kết quả ký', 'chốt · chờ'), ('Result block', 'lock · wait'), 'n sys'),
        ('e1', 4, 'NK', ('Ký ngay', 'trong BPM'), ('Sign now', 'inside BPM')),
        ('f1', 5, 'SYS', ('Đã ký →', 'End'), ('Signed →', 'End'), 'n sys'),
        ('f2', 5, 'LP', ('Từ chối →', 'Trình lại / dừng'), ('Declined →', 'resubmit / stop'), 'n dec'),
    ],
    edges=[
        ('b1', 'c1', 'or'), ('c1', 'c2', 'gr', None, True), ('c1', 'd1', 'or'), ('d1', 'd2', 'gr', None, True),
        ('c2', 'e1', 'gr', ('yêu cầu ký', 'request'), True), ('e1', 'f1', 'gr', ('đã ký', 'signed'), True), ('d2', 'f2', 'rj', ('từ chối', 'declined'), True, 20),
    ],
)

STEPS = [
    dict(id='B1', title=('Làm quen luồng có trình ký', 'Know the signing flow'), app=('BPM', 'BPM'), dur=('3 phút', '3 min'),
         links=[(('Dịch vụ TEST', 'TEST service'), SV + '?view=workflow')],
         w5=[(('Ai', 'Who'), ('Mọi người dùng dịch vụ', 'All service users')), (('Làm gì', 'What'), ('Đọc luồng: bước nào trình ký, bước nào chờ ký', 'Read which step submits and which waits')), (('Ở đâu', 'Where'), ('Dịch vụ › tab Quy trình', 'Service › Flow tab')),
             (('Khi nào', 'When'), ('Trước khi tạo phiếu đầu tiên', 'Before the first job')), (('Vì sao', 'Why'), ('Biết phiếu kẹt ở đâu', 'Know where jobs get stuck')), (('Thế nào', 'How'), ('4 khối, 2 nhánh', '4 blocks, 2 branches'))],
         ai=('Hỏi Trợ lý AI của dịch vụ: “Luồng này có mấy bước ký, ai ký?”', 'Ask the service AI: “How many signing steps, who signs?”'),
         acts=[(('Luồng mẫu: <b>Kế toán trình ký</b> ① (bước có người, có liên kết ký) → <b>Kết quả ký Giám đốc</b> ② (tự động chờ ký) → nhánh <b>Đã ký</b> tới End, <b>Từ chối</b> kết thúc ③.', 'Sample flow: <b>Kế toán trình ký</b> ① (human step with a signing link) → <b>Kết quả ký</b> ② (waits) → <b>Signed</b> to End, <b>Declined</b> ends ③.'), 'bpm_luong_hoanchinh')],
         after=('Người lập sang B2.', 'Requesters go to B2.'), errs=['p01'], done=[('Biết bước trình ký và bước chờ ký', 'You know the submit and wait steps')]),
    dict(id='B2', title=('Tạo công việc kèm tờ trình', 'Create the job with the memo'), app=('BPM', 'BPM'), dur=('2 phút', '2 min'),
         links=[(('Dịch vụ TEST', 'TEST service'), SV)],
         w5=[(('Ai', 'Who'), ('Kế toán / người lập', 'Accountant / requester')), (('Làm gì', 'What'), ('Tạo công việc, tải tờ trình', 'Create the job, upload the memo')), (('Ở đâu', 'Where'), ('+ Công việc mới', '+ Công việc mới')),
             (('Khi nào', 'When'), ('Khi có đề nghị thanh toán', 'When a payment request arises')), (('Vì sao', 'Why'), ('Tệp ở trường này là tệp sẽ được ký', 'This file is what gets signed')), (('Thế nào', 'How'), ('Ưu tiên PDF', 'Prefer PDF'))],
         ai=('Dùng “Điền bằng AI” trên bước để điền trường từ tệp tờ trình.', 'Use “Điền bằng AI” to fill fields from the memo.'),
         acts=[(('Nhập <b>Tiêu đề</b> ①, tải tệp vào trường <b>Tờ trình ký</b> ② (PDF), bấm <b>Tạo công việc</b> ③.', 'Enter the <b>title</b> ①, upload to <b>Tờ trình ký</b> ② (PDF), click <b>Tạo công việc</b> ③.'), 'bpm_tao_cv')],
         after=('Phiếu tự sang bước Kế toán trình ký (B3).', 'The job moves to the submit step (B3).'), errs=['p02'], done=[('Có tệp ở trường Tờ trình ký', 'File in Tờ trình ký')]),
    dict(id='B3', title=('Bấm Trình ký', 'Click Trình ký'), app=('BPM → E-Sign', 'BPM → E-Sign'), dur=('2 phút', '2 min'),
         links=[(('Dịch vụ TEST', 'TEST service'), SV)],
         w5=[(('Ai', 'Who'), ('Người được giao bước Kế toán trình ký', 'Assignee of the submit step')), (('Làm gì', 'What'), ('Tạo yêu cầu ký Giám đốc', 'Create the Director signing request')), (('Ở đâu', 'Where'), ('Chi tiết công việc › nút + Trình ký', 'Job detail › + Trình ký')),
             (('Khi nào', 'When'), ('Khi tờ trình đã đúng', 'When the memo is final')), (('Vì sao', 'Why'), ('Người ký, tài liệu, lời nhắn đã cấu hình sẵn', 'Signer, document, message pre-configured')), (('Thế nào', 'How'), ('Hộp thoại → E-Sign đặt trường → Gửi', 'Dialog → place field → send'))],
         ai=('Trợ lý AI: “Tóm tắt tờ trình để ghi vào lời nhắn cho Giám đốc”.', 'AI: “Summarize the memo for the message”.'),
         acts=[(('Ở bước <b>Kế toán trình ký</b>, bấm <b>+ Trình ký: Trình ký Giám đốc</b> ①. Tệp tờ trình ở ②.', 'At <b>Kế toán trình ký</b>, click <b>+ Trình ký: Trình ký Giám đốc</b> ①. The memo is at ②.'), 'bpm_cv_nut_trinhky'),
               (('Hộp thoại lấy sẵn tên ①, người ký ②, tài liệu ③ từ cấu hình. <b>Gửi ngay khi văn bản đã đủ vị trí ký</b> ④: tệp có mã đặt trường thì gửi thẳng; không thì mở trình đặt trường. Bấm <b>Gửi ký</b> ⑤.', 'The dialog pre-fills name ①, signer ②, documents ③. <b>Gửi ngay…</b> ④: with anchors it sends directly, otherwise opens the field editor. Click <b>Gửi ký</b> ⑤.'), 'bpm_trinhky_hopthoai'),
               (('E-Sign mở ngay trong BPM: tài liệu ①, người ký ②. Bấm <b>Tiếp — Đặt trường</b> ③.', 'E-Sign opens inside BPM: document ①, signer ②. Click <b>Tiếp — Đặt trường</b> ③.'), 'bpm_trinhky_esign_b1'),
               (('Kéo <b>Chữ ký</b> ① vào chỗ ký ②, rồi <b>Xem lại & gửi</b> ③ → Gửi hồ sơ ký.', 'Drag <b>Chữ ký</b> ① to the spot ②, then <b>Xem lại & gửi</b> ③ → send.'), 'bpm_trinhky_dattruong'),
               (('Tab <b>Liên kết</b>: yêu cầu <b>Trình ký Giám đốc</b> ① đã tạo, nút <b>Ký ngay</b> ② cho người ký, trạng thái <b>Đang chờ bạn · 0/1</b> ③.', '<b>Liên kết</b> tab: request ① created, <b>Ký ngay</b> ②, status <b>waiting · 0/1</b> ③.'), 'bpm_cv_lienket_cho')],
         after=('Submit bước để phiếu sang Kết quả ký (B4).', 'Submit the step so the job waits (B4).'), errs=['p03', 'p04', 'p05'], done=[('Yêu cầu ký ở trạng thái Đang chờ', 'Request is waiting')]),
    dict(id='B4', title=('Submit sang chờ ký', 'Submit to wait for signatures'), app=('BPM', 'BPM'), dur=('30 giây', '30 sec'),
         links=[(('Dịch vụ TEST', 'TEST service'), SV)],
         w5=[(('Ai', 'Who'), ('Người lập', 'Requester')), (('Làm gì', 'What'), ('Hoàn thành bước trình ký', 'Complete the submit step')), (('Ở đâu', 'Where'), ('Thẻ Cần bạn xử lý › Submit', 'Cần bạn xử lý › Submit')),
             (('Khi nào', 'When'), ('Ngay sau khi gửi ký', 'Right after sending')), (('Vì sao', 'Why'), ('Kết quả ký chỉ gom yêu cầu khi phiếu vào bước', 'The result block only gathers on entry')), (('Thế nào', 'How'), ('Submit → xác nhận', 'Submit → confirm'))],
         ai=('—', '—'),
         acts=[(('Tổng quan có 2 thẻ: <b>Cần bạn ký</b> ① (nếu bạn cũng là người ký) và <b>Cần bạn xử lý</b>. Bấm <b>Submit</b> ②.', 'Overview shows <b>Cần bạn ký</b> ① and <b>Cần bạn xử lý</b>. Click <b>Submit</b> ②.'), 'bpm_cv_canbanky'),
               (('Phiếu ở bước <b>Kết quả ký Giám đốc</b> ①: “Đang chờ Trình ký Giám đốc · đã ký 0/1” ②. Người ký bấm <b>Ký ngay</b> ③.', 'The job is at <b>Kết quả ký</b> ①: “waiting · 0/1” ②. Signer clicks <b>Ký ngay</b> ③.'), 'bpm_cv_chokyketqua')],
         after=('Người ký ký (B5).', 'The signer signs (B5).'), errs=['p06'], done=[('Phiếu ở bước Kết quả ký', 'Job at the result block')]),
    dict(id='B5', title=('Người ký ký ngay trong BPM', 'Signer signs inside BPM'), app=('BPM · E-Sign', 'BPM · E-Sign'), dur=('1 phút', '1 min'),
         links=[(('E-Sign · Chờ tôi ký', 'E-Sign · Awaiting me'), ES + '/envelopes')],
         w5=[(('Ai', 'Who'), ('Giám đốc', 'Director')), (('Làm gì', 'What'), ('Đọc tờ trình, áp chữ ký', 'Read, apply signature')), (('Ở đâu', 'Where'), ('Công việc › Ký ngay, hoặc email E-Sign', 'Job › Ký ngay, or E-Sign email')),
             (('Khi nào', 'When'), ('Trước hạn ký', 'Before expiry')), (('Vì sao', 'Why'), ('Ký xong phiếu tự đi tiếp', 'The job continues on its own')), (('Thế nào', 'How'), ('Chữ ký lưu sẵn, 1 chạm', 'Saved signature, one click'))],
         ai=('Hỏi Copilot về số tiền, NCC trước khi ký.', 'Ask Copilot about amount and supplier before signing.'),
         acts=[(('Màn ký: <b>Lời nhắn cho bạn</b> ① lấy từ cấu hình liên kết, <b>Ký với danh nghĩa</b> ②. Bấm <b>Xem tài liệu & bắt đầu</b> ③ (hoặc Từ chối ký).', 'Signing screen: <b>message</b> ①, <b>signing as</b> ②. Click <b>Xem tài liệu & bắt đầu</b> ③ (or decline).'), 'bpm_ky_tailieu'),
               (('Bấm ô ký: chữ ký lưu sẵn tự áp ①. Cách ký Rework Sign, đổi bằng Chuyển ②. Bấm <b>Ký ngay</b> ③.', 'Click the field: saved signature applied ①. Rework Sign, change with Chuyển ②. Click <b>Ký ngay</b> ③.'), 'bpm_ky_apchuky')],
         after=('Kết quả ký nhận chữ ký, rẽ nhánh Đã ký (B6).', 'The result block branches Signed (B6).'), errs=['p07', 'p08'], done=[('Bạn đã ký tài liệu', 'You signed')]),
    dict(id='B6', title=('Kết quả ký & hoàn thành', 'Result & completion'), app=('BPM', 'BPM'), dur=('tự động', 'automatic'),
         links=[(('Dịch vụ TEST', 'TEST service'), SV)],
         w5=[(('Ai', 'Who'), ('Hệ thống; người lập kiểm tra', 'System; requester checks')), (('Làm gì', 'What'), ('Phiếu đi tiếp theo nhánh', 'Job follows the branch')), (('Ở đâu', 'Where'), ('Chi tiết công việc', 'Job detail')),
             (('Khi nào', 'When'), ('Ngay khi đủ chữ ký', 'As soon as all signed')), (('Vì sao', 'Why'), ('Không ai phải bấm chuyển bước', 'Nobody needs to move it')), (('Thế nào', 'How'), ('Đã ký → End; Từ chối → dừng/Trình lại', 'Signed → End; Declined → stop/resubmit'))],
         ai=('Lịch sử ghi: ai ký, lúc nào, cách ký.', 'History records who, when, how.'),
         acts=[(('Ký xong, phiếu <b>Đã hoàn thành</b> ① ở bước <b>End</b> ②; thanh tiến trình đủ 4 bước ③.', 'Signed: <b>Đã hoàn thành</b> ① at <b>End</b> ②; all steps done ③.'), 'bpm_cv_hoanthanh'),
               (('Tab Liên kết: <b>Đã chốt ở bước Kết quả ký</b> ①, yêu cầu <b>Đã hoàn thành · 1/1</b> ②.', 'Liên kết tab: <b>locked at the result block</b> ①, request <b>completed 1/1</b> ②.'), 'bpm_cv_lienket_daky')],
         after=('Bản đã ký nằm trong E-Sign và gắn ở tab Liên kết. Nếu cấu hình ghi trường, bản ký/ngày ký ghi về phiếu.', 'The signed copy lives in E-Sign and is linked; write-back fills job fields if configured.'), errs=['p09', 'p10'], done=[('Phiếu Đã hoàn thành', 'Job completed')]),
]

ISSUES = [
    dict(id='p01', roles=['LP', 'TD'], step='B1', img='bpm_luong_hoanchinh', tag=('Luồng', 'Flow'), q=('Luồng có cảnh báo “vấn đề về luồng”', 'The flow shows “flow issue” warnings'),
         cause=('Khối Kết quả ký chưa chọn liên kết, hoặc nhánh chưa nối.', 'Result block has no link, or a branch is unwired.'), fix=('Quản trị mở badge vấn đề, chọn liên kết ở Kết quả ký và nối nhánh Đã ký (S7, S8).', 'Admin fixes per S7, S8.'), kw='van de ve luong canh bao chua noi'),
    dict(id='p02', roles=['LP'], step='B2', img='bpm_tao_cv', tag=('Tệp', 'Files'), q=('Không có ô tải tờ trình khi tạo công việc', 'No memo upload when creating'),
         cause=('Trường File chưa bật “Hiện trên form”.', 'The File field isn’t shown on forms.'), fix=('Quản trị bật Show on forms cho trường Tờ trình ký (S3).', 'Admin enables it (S3).'), kw='khong co o tai to trinh truong file'),
    dict(id='p03', roles=['LP', 'QT'], step='B3', img='bpm_cv_nut_trinhky', tag=('Trình ký', 'Signing'), q=('Không thấy nút + Trình ký trên công việc', 'No + Trình ký button on the job'),
         cause=('Liên kết chưa bật Thủ công / Tự động ở bước hiện tại, hoặc bạn không phải người được giao.', 'Link not enabled on this step, or you’re not the assignee.'), fix=('Quản trị: bước › tab Liên kết › tick Thủ công (S6).', 'Admin: step › Liên kết tab › tick Thủ công (S6).'), kw='khong thay nut trinh ky lien ket thu cong'),
    dict(id='p04', roles=['LP'], step='B3', img='bpm_trinhky_hopthoai', tag=('Trình ký', 'Signing'), q=('Hộp Trình ký không có tài liệu', 'The signing dialog has no document'),
         cause=('Trường tài liệu cấu hình trong liên kết đang trống trên phiếu.', 'The configured document field is empty.'), fix=('Tải tệp vào trường Tờ trình ký rồi bấm lại; hoặc tải trực tiếp trong E-Sign.', 'Upload into the field first, or add in E-Sign.'), kw='khong co tai lieu trinh ky trong'),
    dict(id='p05', roles=['LP'], step='B3', img='bpm_trinhky_dattruong', tag=('Đặt trường', 'Fields'), q=('Bấm Gửi ký nhưng lại phải đặt trường', 'After Gửi ký I still have to place fields'),
         cause=('Tệp không có mã đặt trường nên chưa “đủ vị trí ký”.', 'No anchors in the file.'), fix=('Bình thường: kéo ô Chữ ký. Muốn gửi thẳng, dùng mẫu Word có mã {{sig:giam_doc}} theo role_key.', 'Normal; or use a Word template with role-key anchors.'), kw='phai dat truong gui ngay du vi tri ky'),
    dict(id='p06', roles=['LP', 'TD'], step='B4', img='bpm_cv_chokyketqua', tag=('Chờ ký', 'Waiting'), q=('Phiếu ở Kết quả ký nhưng báo 0 yêu cầu', 'At the result block but 0 requests'),
         cause=('Submit trước khi Trình ký; danh sách chốt “Khi vào bước”.', 'Submitted before creating the request; list locks on entry.'), fix=('Quản trị đổi Chốt danh sách = Thủ công, hoặc kéo phiếu lùi bước, Trình ký rồi Submit lại.', 'Set lock = manual, or move back, submit again.'), kw='ket qua ky 0 yeu cau chot danh sach'),
    dict(id='p07', roles=['NK'], step='B5', img='bpm_ky_tailieu', tag=('Ký', 'Signing'), q=('Tôi muốn từ chối ký', 'I want to decline'),
         cause='—', fix=('Bấm Từ chối ký, ghi lý do. Phiếu đi theo nhánh Từ chối (mặc định kết thúc Thất bại).', 'Click Từ chối ký with a reason; the job follows the decline branch.'), kw='tu choi ky ly do'),
    dict(id='p08', roles=['NK'], step='B5', img='bpm_ky_apchuky', tag=('Ký', 'Signing'), q=('Cần ký bằng USB Token / VGCA', 'Need USB Token / VGCA'),
         cause=('Dịch vụ ký mặc định Rework Sign.', 'Default Rework Sign.'), fix=('Bấm Chuyển trên màn ký; Quản trị E-Sign bật nhà cung cấp.', 'Click Chuyển; E-Sign admin enables providers.'), kw='usb token vgca chuyen cach ky'),
    dict(id='p09', roles=['LP', 'TD', 'QT'], step='B6', img='bpm_ketquaky_tuchoi', tag=('Từ chối', 'Declined'), q=('Bị từ chối ký, muốn trình lại chứ không kết thúc phiếu', 'Declined; want to resubmit instead of ending'),
         cause=('Quy tắc Từ chối mặc định Kết thúc luồng.', 'Default decline rule ends the flow.'), fix=('Quản trị đổi “Sau đó” = Tới bước đã nối, nối về Kế toán trình ký; người ở đó thấy nút Trình lại (S8).', 'Admin routes decline back to the submit step (S8).'), kw='tu choi trinh lai ket thuc luong'),
    dict(id='p10', roles=['LP', 'TD'], step='B6', img='bpm_cv_lienket_daky', tag=('Đồng bộ', 'Sync'), q=('Đã ký trên E-Sign nhưng phiếu vẫn chờ', 'Signed in E-Sign but the job still waits'),
         cause=('Chưa đồng bộ trạng thái.', 'Status not synced yet.'), fix=('Tab Liên kết › bấm Đồng bộ.', 'Liên kết tab › Đồng bộ.'), kw='da ky van cho dong bo'),
]

SETUP = [
    dict(h=('A. Dịch vụ & dữ liệu', 'A. Service & data')),
    dict(id='S1', title=('Tạo dịch vụ', 'Create the service'), img='bpm_dvmoi_1',
         body=('Cài đặt › Dịch vụ › <b>Dịch vụ mới</b>: tên ①, rồi các tab Thành viên, Quyền truy cập, Quyền tạo công việc ②.', 'Settings › <b>New service</b>: name ①, then members, access, creation tabs ②.')),
    dict(id='S2', title=('Thành viên & quyền', 'Members & access'), img='bpm_dvmoi_truycap',
         body=('Chủ dịch vụ ① toàn quyền; người theo dõi ② xem mọi công việc. Quyền tạo công việc: chỉ người được cấp (Kế toán).', 'Owner ① full control; followers ② see all jobs. Restrict job creation.')),
    dict(id='S3', title=('Trường tệp “Tờ trình ký”', 'File field “Tờ trình ký”'), img='bpm_truong_totrinh',
         body=('Trường › Trường mới › <b>Internal</b>: mã <b>custom_to_trinh_ky</b> ① (gõ tay), kiểu <b>Tệp</b> ②. Đây là tệp liên kết ký sẽ lấy.', 'Fields › New › Internal: code ① typed by hand, type <b>File</b> ②.')),
    dict(h=('B. Liên kết Yêu cầu ký (kiểu mới)', 'B. Signing link (new style)')),
    dict(id='S4', title=('Tạo Liên kết Yêu cầu ký', 'Create the signing link'), img='bpm_lienket_tao1',
         body=('Cài đặt dịch vụ › <b>Liên kết</b> › <b>+ Yêu cầu ký</b>. 4 tab ①: Tạo · Người tham gia · Khi yêu cầu ký kết thúc · Khi công việc này kết thúc. Chọn <b>Dịch vụ ký</b> ② (General Signing), <b>Tên yêu cầu</b> ③ có thể dùng {job.name}.', 'Liên kết › + Yêu cầu ký. 4 tabs ①. Pick the signing service ②, name ③ with {job.name}.')),
    dict(id='S5', title=('Người ký, tài liệu, lời nhắn', 'Signers, documents, message'), img='bpm_lienket_vaitroky',
         body=('Người trình ① = người tạo công việc. Thêm người ký: vai trò ② (vd Giám đốc), chọn người, kiểu <b>Ký / Phê duyệt (không ký) / Ký trực tiếp</b> ③. Tài liệu: Mẫu in hoặc <b>Trường tài liệu</b> = Tờ trình ký. Lời nhắn hiện trên màn ký. Bấm <b>Tạo liên kết</b>.', 'Submitter ① = job creator. Add signer role ②, person, type ③. Document = Tờ trình ký field. Message shown to signer.')),
    dict(id='S6', title=('Bật liên kết ở bước', 'Enable the link on a step'), img='bpm_buoc_lienket_thucong',
         body=('Trình dựng › bước <b>Kế toán trình ký</b> › tab <b>Liên kết</b> ①. Ở dòng Trình ký Giám đốc ② tick <b>Thủ công</b> ③ (người ở bước bấm tạo) hoặc <b>Tự động</b> (tạo ngay khi vào bước).', 'Builder › step › <b>Liên kết</b> tab ①. On the link row ② tick <b>Thủ công</b> ③ or <b>Tự động</b>.')),
    dict(id='S7', title=('Khối Kết quả ký', 'Signing-result block'), img='bpm_ketquaky_hoantat',
         body=('Palette › Ứng dụng nội bộ › <b>Kết quả ký</b>. Chọn liên kết cần gom, <b>Chốt danh sách</b> ① = Khi vào bước (chỉ xét yêu cầu đã có) hoặc Thủ công. Hoàn tất có 2 quy tắc: Đã ký, Từ chối.', 'Palette › <b>Kết quả ký</b>. Pick links, <b>lock</b> ① on entry or manual. Two rules: Signed, Declined.')),
    dict(id='S8', title=('Nhánh Từ chối & Trình lại', 'Decline branch & resubmit'), img='bpm_ketquaky_tuchoi',
         body=('Quy tắc Từ chối ①: <b>Kết thúc luồng</b> ② (Thất bại) hoặc <b>Tới bước đã nối</b> → nối về bước có người, bật liên kết Thủ công để thấy nút <b>Trình lại</b> ③.', 'Decline ①: <b>end</b> ② or route to a human step with the link on to get <b>Trình lại</b> ③.')),
    dict(id='S9', title=('Nối luồng & kiểm tra', 'Wire & validate'), img='bpm_luong_hoanchinh',
         body=('Start → Kế toán trình ký ① → Kết quả ký ② → Đã ký → End ③. Xoá cạnh thừa Start → End. Badge vấn đề phải về 0, rồi chạy 1 phiếu TEST. Khối cũ <b>Chữ ký điện tử</b> (nhãn “Kiểu cũ”) vẫn chạy nhưng nên dùng kiểu mới.', 'Start → submit ① → result ② → Signed → End ③. Remove stray edges; zero issues; run a TEST job. The old e-signature block still works.')),
]
CHECKLIST = [
    ('Có trường File cho tài liệu ký, hiện trên form.', 'A File field for the document, on forms.'),
    ('Liên kết Yêu cầu ký: đúng dịch vụ ký, người ký, trường tài liệu, lời nhắn.', 'Link: right service, signer, document field, message.'),
    ('Bước trình ký bật liên kết Thủ công hoặc Tự động.', 'Submit step enables the link.'),
    ('Khối Kết quả ký gom đúng liên kết; nhánh Đã ký và Từ chối đã nối.', 'Result block gathers the link; both branches wired.'),
    ('Badge vấn đề luồng = 0.', 'Flow issues = 0.'),
    ('Chạy 1 phiếu TEST đến End, rồi 1 phiếu thử Từ chối.', 'Run a TEST job to End, and one decline.'),
]
AI_QS = [
    ('LP', ('Tóm tắt tờ trình trong 3 dòng để làm lời nhắn cho Giám đốc.', 'Summarize the memo in 3 lines for the Director.')),
    ('NK', ('Đề nghị này có gì khác so với kỳ trước?', 'What changed versus last period?')),
    ('TD', ('Những phiếu nào đang chờ ký quá 2 ngày?', 'Which jobs have waited for signatures over 2 days?')),
    ('QT', ('Kiểm tra luồng: bước nào chưa nối, khối Kết quả ký đã gom liên kết nào?', 'Validate: unwired steps, which links the result block gathers?')),
]
AIMAP = dict(
    map=[(('Điền bằng AI', 'Fill with AI'), ('Đọc tệp đính kèm, điền trường trên bước.', 'Reads attachments, fills step fields.')),
         (('Trợ lý AI dịch vụ', 'Service AI assistant'), ('Hỏi về phiếu, luồng, thống kê.', 'Ask about jobs, flow, stats.')),
         (('Xây bằng AI', 'Build with AI'), ('Mô tả quy trình, AI dựng khung luồng.', 'Describe a process, AI drafts the flow.'))],
    figs=[('bpm_tao_cv', ('Form tạo công việc', 'Create form')), ('bpm_luong_hoanchinh', ('Luồng có trình ký', 'Flow with signing'))],
    rules=[('AI gợi ý, người bấm Trình ký / Ký.', 'AI suggests; people submit and sign.'),
           ('Kiểm tra số tiền AI điền.', 'Check amounts AI fills.'),
           ('Không dán mật khẩu, số tài khoản.', 'No passwords or account numbers.'),
           ('Dùng Xây bằng AI để phác, quản trị kiểm từng khối.', 'Use Build with AI for drafts; check every block.'),
           ('Câu hỏi tốt = phiếu nào + muốn biết gì.', 'Good prompt = which job + what.')],
)
AIBLK = dict(title=('Ký ngay trong phiếu, ký xong phiếu tự chạy', 'Sign inside the job; it moves on by itself'),
             desc=('Ảnh thật trên phiếu TEST #18741: gửi 00:26, ký và hoàn thành 00:27.', 'Real TEST job #18741: sent 00:26, signed and completed 00:27.'),
             kpi=[('~1', ('phút từ trình đến hoàn thành', 'min submit to done'), ('Chắc chắn', 'Certain')), ('0', ('lần bấm chuyển bước sau khi ký', 'manual moves after signing'), ('Chắc chắn', 'Certain')), ('-60%', ('thời gian duyệt chi', 'payment approval time'), ('Mục tiêu', 'Target'))],
             imgs=['bpm_cv_canbanky', 'bpm_cv_hoanthanh'])
BEN = [
    ('bpm_cv_canbanky', ('Biết ngay việc cần ký', 'See what to sign'), ('Thẻ “Cần bạn ký” hiện trên phiếu cho đúng người ký.', '“Cần bạn ký” card for the right signer.'), ('Chắc chắn', 'Certain'), ('1 chạm Ký ngay', 'One-click Ký ngay'), ('Gửi file qua chat, chờ phản hồi', 'Files over chat')),
    ('bpm_cv_hoanthanh', ('Ký xong tự hoàn thành', 'Auto-complete when signed'), ('Kết quả ký nhận chữ ký và đẩy phiếu sang End.', 'The result block moves the job to End.'), ('Chắc chắn', 'Certain'), ('Trình 00:26 → Xong 00:27', 'Sent 00:26 → done 00:27'), ('Nhắc nhau chuyển bước', 'Chasing step moves')),
    ('bpm_cv_lienket_daky', ('Lưu vết đầy đủ', 'Full audit trail'), ('Tab Liên kết giữ yêu cầu ký, người ký, trạng thái.', 'Liên kết tab keeps requests, signers, status.'), ('Mục tiêu', 'Target'), ('100% phiếu chi có bản ký', '100% payments with signed memo'), ('Bản ký tay thất lạc', 'Lost paper copies')),
]
IMG_LINK = {'bpm_luong_hoanchinh': BUILD, 'bpm_tao_cv': SV, 'bpm_cv_canbanky': SV, 'bpm_cv_hoanthanh': SV, 'bpm_cv_lienket_daky': SV, 'bpm_dvmoi_1': SET}
