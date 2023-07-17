import json

def parse_instruction_document() -> list[str]:
    instructions: list[str] = []

    with open("instructions.txt", "r") as file:
        lines = file.readlines()
        
        for i, line in enumerate(lines):
            if (line[0] == "#" or line[0] == '\n'):
                continue
            
            index_to_remove = line.find(" ")
            instruction = line[:index_to_remove]
            instructions.append(instruction)

    return list(set(instructions))

def create_instruction_json_file(instructions: list[str]):
    with open("./instructions.json", "w") as tmp:
        tmp.write("")
    
    with open("./instructions.json", "a") as file:
        group = 1
        instruction_group = ""

        file.write("[")

        for i, instruction in enumerate(instructions):
            separator = "|"
            instruction_group += instruction + separator

            if i % 20 == 0 and i != 0:
                file.write("\n")
                list_instruction_group = list(instruction_group) # Convert to list since strings are immutable
                list_instruction_group.pop() # Remove the last seperator to avoid problems
                instruction_group = "".join(list_instruction_group) # Restore it to a string
                data = { "name": f"keyword.instructions.group{group}", "match": f"\\b(?i:{instruction_group})\\b" }
                instruction_group = "" # Reset the group back to nothing
                json.dump(data, file)
                file.write(",")
                group += 1
        
        file.write("\n]")             

            
def main():
    instructions: list[str] = parse_instruction_document()
    create_instruction_json_file(instructions)

if __name__ == "__main__":
    main()