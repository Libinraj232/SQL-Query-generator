import gradio as gr

# SELECT Query
def generate_select(table, columns):
    cols = [c.strip() for c in columns.split(",")]
    query = f"SELECT {', '.join(cols)} FROM {table};"
    return query

# INSERT Query
def generate_insert(table, columns):
    cols = [c.strip() for c in columns.split(",")]
    values = ", ".join(["%s"] * len(cols))
    query = f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({values});"
    return query

# UPDATE Query
def generate_update(table, columns, condition):
    cols = [c.strip() for c in columns.split(",")]
    set_part = ", ".join([f"{c}=%s" for c in cols])
    query = f"UPDATE {table} SET {set_part} WHERE {condition};"
    return query

# DELETE Query
def generate_delete(table, condition):
    query = f"DELETE FROM {table} WHERE {condition};"
    return query


# Gradio Functions
def select_ui(table, columns):
    return generate_select(table, columns)

def insert_ui(table, columns):
    return generate_insert(table, columns)

def update_ui(table, columns, condition):
    return generate_update(table, columns, condition)

def delete_ui(table, condition):
    return generate_delete(table, condition)


# UI Layout
with gr.Blocks() as app:
    gr.Markdown("# SQL Query Generator")

    with gr.Tab("SELECT"):
        table = gr.Textbox(label="Table Name")
        columns = gr.Textbox(label="Columns (comma separated)")
        output = gr.Textbox(label="Generated Query")
        btn = gr.Button("Generate SELECT")
        btn.click(select_ui, inputs=[table, columns], outputs=output)

    with gr.Tab("INSERT"):
        table2 = gr.Textbox(label="Table Name")
        columns2 = gr.Textbox(label="Columns")
        output2 = gr.Textbox(label="Generated Query")
        btn2 = gr.Button("Generate INSERT")
        btn2.click(insert_ui, inputs=[table2, columns2], outputs=output2)

    with gr.Tab("UPDATE"):
        table3 = gr.Textbox(label="Table Name")
        columns3 = gr.Textbox(label="Columns")
        condition = gr.Textbox(label="Condition (example: id=1)")
        output3 = gr.Textbox(label="Generated Query")
        btn3 = gr.Button("Generate UPDATE")
        btn3.click(update_ui, inputs=[table3, columns3, condition], outputs=output3)

    with gr.Tab("DELETE"):
        table4 = gr.Textbox(label="Table Name")
        condition2 = gr.Textbox(label="Condition")
        output4 = gr.Textbox(label="Generated Query")
        btn4 = gr.Button("Generate DELETE")
        btn4.click(delete_ui, inputs=[table4, condition2], outputs=output4)

app.launch(share=True)
