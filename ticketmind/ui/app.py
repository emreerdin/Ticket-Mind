import streamlit as st
import pandas as pd
from ticketmind.db.repos import tickets_repo
from ticketmind.agent.states import TicketState
from ticketmind.agent.contracts import ticket_input
st.set_page_config(
    page_title="Ticket Mind",
    layout="wide"
)

ordered_tickets = tickets_repo.get_open_tickets()

ordered_tickets_df = pd.DataFrame(ordered_tickets)
st.table(ordered_tickets_df.loc[0])

