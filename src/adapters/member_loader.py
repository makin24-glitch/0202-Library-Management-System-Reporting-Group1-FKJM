 # adapters/member_loader.py

from member import Member


def load_sample_members(sample_records):
    """
    Adapter: raw member records → Member objects.

    Returns:
        dict[str, Member]: keyed by member_id
    """
    members = {}

    for record in sample_records:
        member = Member(
            member_id=record["member_id"],
            name=record["name"],
            email=record["email"],
            join_date=record["join_date"]
        )
        members[member.member_id] = member

    return members
