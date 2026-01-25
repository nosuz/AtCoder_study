package abc437;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

class BTest {

    private static String stripLastNewline(String s) {
        // 末尾の改行だけを1個除去（\n / \r\n 対応）
        return s.replaceFirst("\\R\\z", "");
    }

    private static String show(String s) {
        // 見比べやすい表示（改行を可視化）
        return s.replace("\r", "\\\\r").replace("\n", "⏎\\n");
    }


    @Test
    void sample1() {
        String input = "3 4 5\n12 3 5 7\n6 10 11 9\n1 2 4 8\n2\n4\n9\n6\n11";
        String expected = "3";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            B.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


    @Test
    void sample2() {
        String input = "3 5 2\n81 63 31 16 15\n30 3 6 54 24\n26 41 48 64 66\n44\n79";
        String expected = "0";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            B.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


    @Test
    void sample3() {
        String input = "3 5 12\n78 19 70 58 83\n12 30 80 20 27\n48 71 8 43 82\n82\n30\n43\n8\n80\n70\n20\n78\n12\n71\n19\n48";
        String expected = "5";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            B.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


}
