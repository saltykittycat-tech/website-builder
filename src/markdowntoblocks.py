
def markdown_to_blocks(markdown):
    md = markdown.split("\n\n")
    final_blocks = []
    for block in md:
        new_block = block.strip()
        final_blocks.append(new_block)
    for i in range(len(final_blocks)):
        if final_blocks[i] == "":
            del final_blocks[i]
    #print(f"final blocks: {final_blocks}")
    return final_blocks
